from django.db import models
from django.utils import timezone


class InitialStock(models.Model):
    stockInitial = models.IntegerField(default=0)
    deleveredAt = models.DateTimeField(default=timezone.now)

class Stock(models.Model):
    quantity = models.IntegerField(default=0)
    deleveredAt = models.DateTimeField(default=timezone.now)
    designation = models.CharField(max_length=255)

class Command(models.Model):
    designation = models.CharField(max_length=255)
    retour = models.IntegerField(blank=True, null=True, default=0)
    sortie = models.IntegerField(blank=True, null=True, default=0)
    deliveredAt = models.DateTimeField(default=timezone.now)
    stockCourant = models.IntegerField(default=0)