from django.contrib import admin

# Register your models here.
from .models import cusinfo, customer, admin4, product, supplier, images12,categories,  cart, order, ordetails, billing
admin.site.register(cusinfo)
admin.site.register(customer)
admin.site.register(admin4)
admin.site.register(product)
admin.site.register(supplier)
admin.site.register(images12)
admin.site.register(categories)
admin.site.register(cart)
admin.site.register(order)
admin.site.register(ordetails)
admin.site.register(billing)