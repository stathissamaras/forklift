from django.contrib import admin


# Register your models here.
from .models import Admin, Order, CartProduct, Cart, Product, Make, Model_type, Car_type, Category, Customer


# Register your models here.

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'full_name',)
    list_filter = ('user', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cart', 'ordered_by', 'mobile', 'subtotal',)
    search_fields = ('order_status', )
    list_filter = ('order_status', )

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cart', 'product', 'quantity', 'subtotal',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total',)
    list_filter = ('customer', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'marked_price', 'selling_price', 'available',)
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(Make)
class StateAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ('name', )


@admin.register(Model_type)
class CityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'make')
    search_fields = ('name', 'make_name' )
    list_filter = ('make',)


@admin.register(Car_type)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'model_type')
    search_fields = ('name', 'model__name')
    list_filter = ('model_type',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'car_type')
    search_fields = ('name', 'car_type__name')
    list_filter = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'full_name', 'address',)
    list_filter = ('full_name', 'address',)
    
