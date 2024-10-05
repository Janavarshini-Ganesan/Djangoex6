from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createtab/', views.create1, name='createtab'),
    path('readtab/', views.read, name='readtab'),
    path('<int:pk>/updatetab/', views.update, name='updatetab'),
    path('<int:pk>/deletetab/', views.delete, name='deletetab'),
    path('delete_confirmation/', views.delete_confirmation, name='delete_confirmation'),
    path('delete_confirm/', views.delete_confirm, name='delete_confirm'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('success_create/', views.success_create, name='success_create'),  # Success after creation
    path('success_delete/', views.success_delete, name='success_delete'),  # Success after deletion
]
