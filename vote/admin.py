from django.contrib import admin

from .models import Category, Places


# Register your models here.
class PlacesAdminTabularInline(admin.TabularInline):
    model = Places
    extra = 1

@admin.register(Category)
class CategoryAdminRegister(admin.ModelAdmin):
    list_display = ['id','name']
    list_editable = ['name']
    search_fields = ['name','id','date']
    inlines = [PlacesAdminTabularInline]

@admin.register(Places)
class PlacesAdminRegister(admin.ModelAdmin):
    list_display = ['id','name','vote','percent']
    list_editable = ['name']
    search_fields = ['name','vote']
    list_filter = ['id']