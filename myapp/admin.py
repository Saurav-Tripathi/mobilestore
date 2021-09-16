from django.contrib import admin
from .models import Registration,Category,Product
from .models import Cart
# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display =['name','number','email','password']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name']

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display =['id','cat','name','price','dis_price','img','des']

@admin.register(Cart)   
class add_to_CartAdmin(admin.ModelAdmin):
    list_display =['user','prod','quantity','subtotal']
