from django.contrib import admin
from  .models import Product, Subcategory, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Subcategory)
admin.site.register(Category)
