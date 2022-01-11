from django.contrib import admin
from .models import Category
# Register your models here.

# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'cat_image')
    prepopulated_fields = {'slug': ('category_name',)}
