from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard', views.dashboard, name='dashboard'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_view, name='logout'),
]