from django.db import models

class AgendaPrivada(models.Model):
    Nome = models.CharField(max_length=64)
    Compromisso = models.TextField()
    Data = models.DateTimeField()

class AgendaPublica(models.Model):
    Nome = models.CharField(max_length=64)
    Compromisso = models.TextField()
    Data = models.DateTimeField()

class AgendaInstitucional(models.Model):
    Nome = models.CharField(max_length=64)
    Feriado = models.CharField(max_length=64)
    Data = models.DateField()