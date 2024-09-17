from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enterprise = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    tel = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    positon_enterprise = models.CharField(max_length=30, blank=True, null=True)
    andress = models.CharField(max_length=40)
    cep = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    admin = models.BooleanField()
