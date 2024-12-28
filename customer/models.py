from django.db import models

class Customer(models.Model):
    class Meta:
        db_table = "crm_customer"
    company = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    tel = models.CharField(max_length=12)
    website= models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=20)
    state= models.CharField(max_length=20)
    country = models.CharField(max_length=20)