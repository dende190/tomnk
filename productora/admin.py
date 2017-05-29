from django.contrib import admin
from .models import Banda, Tomnk

# Register your models here.

@admin.register(Banda)
class AdminBanda(admin.ModelAdmin):
	list_display = ('id', 'name',)

@admin.register(Tomnk)
class AdminTomnk(admin.ModelAdmin):
	list_display = ('id', 'name',)