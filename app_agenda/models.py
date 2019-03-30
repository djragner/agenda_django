from django.db import models

class AgendaPrivada(models.Model):
    class Meta:
        verbose_name = 'Agenda Privada'
        verbose_name_plural = 'Agenda Privada'

    Nome = models.CharField('Nome do médico', max_length=64)
    Compromisso = models.TextField('Tipo de compromisso', max_length=128)
    Data = models.DateTimeField()

class AgendaPublica(models.Model):
    class Meta:
        verbose_name = 'Agenda Pública'
        verbose_name_plural = 'Agenda Pública'

    Nome = models.CharField('Nome do Médico', max_length=64)
    Compromisso = models.TextField('Tipo de compromisso', max_length=128)
    Data = models.DateTimeField()

class AgendaInstitucional(models.Model):
    class Meta:
        verbose_name = 'Agenda Institucional'
        verbose_name_plural = 'Agenda Institucional'

    Nome = models.CharField('Nome Médico', max_length=64)
    Feriado = models.CharField('Nome do feriado', max_length=64)
    Data = models.DateField()