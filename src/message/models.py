from django.db import models
from django.utils import timezone

class TypeDemande(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type


class Service(models.Model):
    libelle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.libelle

class Ordinateur(models.Model):
    reference = models.CharField(max_length=100)
    def __str__(self):
        return self.reference

class Telephone(models.Model):
    reference = models.CharField(max_length=100)
    def __str__(self):
        return self.reference

class Acces(models.Model):
    reference = models.CharField(max_length=100)
    def __str__(self):
        return self.reference

class Employee(models.Model):
    reference = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50, default=None)
    service = models.ForeignKey(Service,on_delete=models.PROTECT, blank=True, null=True)
    password = models.CharField(max_length=100)
    dateStart = models.DateTimeField(default=timezone.now)
    workplace = models.CharField(max_length=50, default=None)
    job = models.CharField(max_length=50, default=None)
    refAcces = models.CharField(max_length=50, null=True, blank=True)
    refOrdi = models.CharField(max_length=50, null=True, blank=True)
    refPhone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name +" " +self.firstName

class Message(models.Model):
    typeDemande = models.ForeignKey(TypeDemande,on_delete=models.PROTECT)
    ordinateur  = models.CharField(max_length=100, blank=True, null=True)
    telephone  = models.CharField(max_length=100, blank=True, null=True)
    acces  = models.CharField(max_length=100, blank=True, null=True)
    description  = models.TextField(blank=True, null=True)
    employe = models.ForeignKey(Employee,on_delete=models.PROTECT)
    sendBy = models.CharField(max_length=10)
    receiver = models.ForeignKey(Service,on_delete=models.PROTECT)
    dateReceiver = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=False)
    file  = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
   

    def __int__(self):
        return self.id


