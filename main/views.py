from django.shortcuts import render
from django.views import generic
from main.models import Brand, Pincode, Product, ProductInstance, OrderDetail, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_products = Product.objects.all().count()
    num_instances = ProductInstance.objects.all().count()
    num_brands = Brand.objects.count()

    context = {
        'num_products': num_products,
        'num_brands': num_brands,
        'num_instances': num_instances,
    }
    return render(request, 'index.html', context=context)


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 8


class BrandListView(generic.ListView):
    model = Brand
    paginate_by = 3


class ProductDetailView(generic.DetailView):
    model = Product


class ProductInstanceDetailView(generic.DetailView):
    model = ProductInstance


class BookCreate(CreateView):
    model = OrderDetail
    fields = '__all__'


import datetime
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.forms import OrderForm

def order_item(request, pk):
    product_instance = get_object_or_404(ProductInstance, pk=pk)
    # current_user = get_object_or_404(User, pk=pk)


    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = OrderForm(request.POST)


        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # product_instance.due_back = form.cleaned_data['renewal_date']
            # product_instance.save()
            order_details = OrderDetail()
            user = User.objects.get(id=request.user.id)
            # current_user = request.user
            order_details.user = user
            order_details.uuid = product_instance.id
            order_details.brand = product_instance.title.brand
            order_details.title = product_instance.title
            order_details.price = product_instance.title.price
            order_details.size = product_instance.size
            order_details.address = form.cleaned_data['address']
            order_details.pincode = form.cleaned_data['pincode']
            order_details.panchayath = form.cleaned_data['panchayath']
            order_details.phone_number = form.cleaned_data['phone_number']
            order_details.save()
            product_instance.delete()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('order-placed'))

    # If this is a GET (or any other method) create the default form.
    else:
        # proposed_pincode = "enter pincode"
        form = OrderForm()

    context = {
        'form': form,
        'order_field': product_instance,
    }

    return render(request, 'main/order_detail.html', context)


def order_placed(request):
    return render(request, 'main/order_placed.html')



from django.contrib.auth.mixins import LoginRequiredMixin


class UsercartView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = OrderDetail
    template_name = 'main/user_cart.html'
    paginate_by = 10

    # def get_queryset(self):
    #     return OrderDetail.objects.filter(brand='nikottin')


def user_cart(request):
    item_count = OrderDetail.objects.filter(user=request.user).count()
    my_cart = OrderDetail.objects.filter(user=request.user)
    context={
                'item_count': item_count,
                'my_cart': my_cart,
    }
    return render(request, 'main/user_cart.html', context=context)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})