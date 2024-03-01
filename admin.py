from django.contrib import admin
from .models import Products
# Register your models here.


class flipkartAdmin(admin.ModelAdmin):
    list_display=('pname','price','stock')
admin.site.register(Products,flipkartAdmin)