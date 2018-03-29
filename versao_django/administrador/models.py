from django.db import models

# Create your models here.
class Administrador(models.Model):
    login = models.CharField(max_length=50, blank=False)
    senha = models.CharField(max_length=20, blank=False)
    nomeAdmin = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.login