from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('stock_initial/', views.get_stock_initial, name='stock_initial'),
    path('stock_initial/create/', views.create_initial_stock, name='create_initial_stock'),
    path('stock_initial/<int:stock_id>/delete/', views.delete_stock, name="delete_stock"),
   ]