from django.contrib import admin
from .models import Product, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'updated', 'created']
    list_filter = ['category', 'updated', 'created', 'available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)


