from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'firstName', 'lastName', 'phone', 'fincaName', 'password1', 'password2']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.role = 'farmer'
            if commit:
                user.save()
            return user
