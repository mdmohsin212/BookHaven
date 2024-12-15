from django.contrib import admin
from categories.models import Categorie

# Register your models here.

class AdminSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category',)}
    list_display = ['category', 'slug']

admin.site.register(Categorie, AdminSlug)