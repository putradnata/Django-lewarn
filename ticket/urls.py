from django.urls import path

# import viewnya
from . import views

urlpatterns = [
    path('', views.index, name='ticket-index'),
    path('create/', views.create, name='ticket-create'),
    path('edit/', views.edit, name='ticket-edit')
]

