from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
import uuid # Required for unique book instances


class Pincode(models.Model):
    pin = models.CharField(max_length=6, help_text='Enter Pincode')

    def __str__(self):
        return self.pin


class Product(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=18)
    photo = models.ImageField(upload_to="gallery", null=True)
    price = models.CharField(max_length=6, help_text='Enter Pincode')
    color = models.CharField(max_length=50, null=True)
    pincode = models.ManyToManyField(Pincode, help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin."""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'


class Brand(models.Model):
    name = models.CharField(max_length=20)

    # def get_absolute_url(self):
    #     return reverse('-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    title = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    AVAILABLE_SIZE = (
        ('Extra Small', 'Extra Small'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),
    )

    size = models.CharField(
        max_length=20,
        choices=AVAILABLE_SIZE,
        blank=True,
        default='S',
        help_text='Book availability',
    )

    def __str__(self):
        return f'{self.id}'
    #
    # def get_absolute_url(self):
    #     return reverse('productinstance', args=[str(self.id)])

from django.contrib.auth.models import User


class OrderDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    uuid = models.CharField(max_length=100, null= True)
    title = models.CharField(max_length=100, null= True)
    brand = models.CharField(max_length=100, null= True)
    price = models.CharField(max_length=100, null= True)
    size = models.CharField(max_length=10, null= True)
    pincode = models.CharField(max_length=6, null=True)
    address = models.TextField(max_length=1000, null= True)
    panchayath = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null= True)
