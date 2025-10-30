from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('farmer', 'Agricultor'),
        ('technician', 'Tecnico de soporte'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='farmer')
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    fincaName = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'