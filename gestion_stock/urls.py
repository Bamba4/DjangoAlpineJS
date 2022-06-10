from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('stock_initial/', views.get_stock_initial, name='stock_initial'),
    path('stock_initial/create/', views.create_initial_stock, name='create_initial_stock'),
    path('stock_initial/<int:stock_id>/delete/', views.delete_stock, name="delete_stock"),
    path('stock_initial/create/stock/', views.create_command, name='create_command'),
    path('stock_initial/all_commands/', views.get_all_commands, name='all_commands'),
    path('stock_initial/all_commands/<int:stock_id>/delete/', views.delete_command, name='delete_command'),
   ]