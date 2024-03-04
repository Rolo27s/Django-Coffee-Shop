from django.contrib import admin
from coffee.models import Coffee

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Coffee, CoffeeAdmin)
