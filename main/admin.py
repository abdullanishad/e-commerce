from django.contrib import admin
from .models import Brand, Pincode, Product, ProductInstance, OrderDetail

admin.site.register(Brand)
admin.site.register(Pincode)
admin.site.register(Product)
admin.site.register(ProductInstance)
admin.site.register(OrderDetail)
