from django.urls import path
from . import views

app_name = 'cultivos'

urlpatterns = [
    path('mis_cultivos/', views.my_cultivos, name='mis_cultivos'),
    path('create_cultivo/', views.create_cultivo, name='create_cultivo'),
    path('edit_cultivo/<int:pk>/', views.edit_cultivo, name='edit_cultivo'),
    path('delete_cultivo/<int:pk>/', views.delete_cultivo, name='delete_cultivo'),
]