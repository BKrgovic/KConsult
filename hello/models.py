from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Firma(models.Model):
    pib = models.IntegerField(primary_key = True)
    naziv = models.CharField(max_length = 256)
    adresa = models.CharField(max_length = 256)
    djelatnost = models.CharField(max_length = 256)

    podrucna_Jedinica = models.CharField(max_length = 256)
    datum_reg = models.DateField()
    Reg_br = models.CharField(max_length = 256)
    Mesto_reg = models.CharField(max_length = 256)
    
    Registrovan_PDV = models.BooleanField()
    Datum_PDV = models.DateField(null = True)
    Broj_PDV = models.CharField(max_length = 256, null=True)

    def __str__(self):
        return self.naziv
    
class Iskaz(models.Model):
    firma = models.ForeignKey(Firma,on_delete=models.CASCADE)
    broj_iskaza = models.CharField (max_length=256)
    godina = models.IntegerField()

