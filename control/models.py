from __future__ import unicode_literals

from django.db import models

class alumno(models.Model):
	numControl = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	semestre = models.IntegerField()
	horas = models.IntegerField()
	extras = models.IntegerField()
	tutorias = models.CharField(max_length=5)

	def __str__(self):
		return str(self.numControl) + ' - ' + self.nombre 

class alumnosAcreditados(models.Model):
	numControl = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	carrera = models.CharField(max_length=50)
	fechaTerminacion = models.CharField(max_length=45)

	def __str__(self):
		return str(self.numControl) + ' - ' + self.carrera

class alumnosPendientes(models.Model):
	numControl = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	carrera = models.CharField(max_length=50)
	semestre = models.IntegerField()

class extraescolares(models.Model):
	numControl = models.IntegerField(primary_key=True)
	extraescolar = models.CharField(max_length=50)
	campusPrimero = models.CharField(max_length=10)
	extraescolar2 = models.CharField(max_length=50)

class extraescolaresDisponibles(models.Model):
	id_Extraescolar = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	CampusExtraescolar = models.CharField(max_length=50)
	campusSegundo = models.CharField(max_length=10)