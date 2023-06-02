from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Carousel)
admin.site.register(CarCategory)
admin.site.register(CarProduct)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)