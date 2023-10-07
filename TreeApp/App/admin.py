from django.contrib import admin
from .models import Menu, MenuCategory

from django.contrib import admin
from .models import Menu, MenuCategory


# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    search_fields = ('name', )
    prepopulated_fields = {
        'slug': ('name',)
    }


class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
