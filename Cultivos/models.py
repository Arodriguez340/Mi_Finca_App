from django.db import models
from users.models import User

class Cultivo(models.Model):

    TYPE_CULTIVO_CHOICES = [
        ('hortaliza', 'Hortaliza'),
        ('frutales', 'Frutales'),
        ('cereales', 'Cereales'),
        ('leguminosas', 'Leguminosas'),
        ('tuberculos', 'Tuberculos')
    ]

    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cultivos')
    nombreCultivo = models.CharField(max_length=50)
    description = models.TextField()
    typeCultivo = models.CharField(choices=TYPE_CULTIVO_CHOICES)

    def __str__(self):
        return f'{self.nombreCultivo} - {self.typeCultivo}'