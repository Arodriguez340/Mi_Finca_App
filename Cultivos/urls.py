from django.urls import path
from . import views

app_name = 'cultivos'

urlpatterns = [
    path('mis_cultivos/', views.my_cultivos, name='mis_cultivos'),
]