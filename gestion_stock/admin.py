from django.contrib import admin
from gestion_stock.models import Stock, InitialStock, Command

# Register your models here.
admin.site.register(InitialStock)
admin.site.register(Stock)
admin.site.register(Command)