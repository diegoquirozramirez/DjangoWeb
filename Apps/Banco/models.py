# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from Apps.Egresos.models import Egresos
#from Apps.Ingresos.models import Ingresos
#from Apps.Personal.models import Personal
from django.contrib.auth.models import User

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Egresos(models.Model):
    egresos = models.FloatField()
    porcentaje =models.FloatField()
    egresos_neto = models.FloatField()

    def __str__(self):
        return '{}'.format(
            self.egresos_neto
        )

class Ingresos(models.Model):
    ingresos = models.FloatField()
    porcentaje = models.FloatField()
    ingresos_neto = models.FloatField()

    def __str__(self):
        return '{}'.format(
            self.ingresos_neto
        )

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50)
    universidad = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    año_egreso = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(
            self.nombre, self.apellidos
        )

class Auditor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(
            self.nombre
        )

class Banco(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=20)
    ruc = models.IntegerField(blank=True)
    fk_egresos = models.ForeignKey(Egresos, on_delete=models.CASCADE)
    fk_ingresos = models.ForeignKey(Ingresos, on_delete=models.CASCADE)
    fk_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(
            self.nombre,
            self.pais,
            self.ruc,
            self.fk_egresos,
            self.fk_ingresos,
            self.fk_personal,
            self.user,
            self.auditor
        )

    def Porcentaje(self):
        procentaje = self.fk_egresos.egresos/self.fk_ingresos.ingresos
        return '{}'.format(procentaje)


    def Millones(self):
        millones = (self.fk_ingresos.ingresos + self.fk_egresos.egresos)/1000000
        return '{}'.format(millones)

    