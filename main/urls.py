from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('productinstance/<int:pk>', views.ProductInstanceDetailView.as_view(), name='product-instance'),
    #path('productinstance/<int:pk>/order/', views.OrderUpdate.as_view(), name='order_update'),
]

urlpatterns += [
    path('products/<uuid:pk>/order/', views.order_item, name='order'),
    path('products/placed/', views.order_placed, name='order-placed'),
    path('mycart/', views.user_cart, name='my-cart'),
]

urlpatterns += [
    path('signup/', views.signup, name='signup'),
]