# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('numControl', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('semestre', models.IntegerField()),
                ('horas', models.IntegerField()),
                ('extras', models.IntegerField()),
                ('tutorias', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='alumnosAcreditados',
            fields=[
                ('numControl', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=50)),
                ('fechaTerminacion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='alumnosPendientes',
            fields=[
                ('numControl', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=50)),
                ('semestre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='extraescolares',
            fields=[
                ('numControl', models.IntegerField(primary_key=True, serialize=False)),
                ('extraescolar', models.CharField(max_length=50)),
                ('campusPrimero', models.CharField(max_length=10)),
                ('extraescolar2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='extraescolaresDisponibles',
            fields=[
                ('id_Extraescolar', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('CampusExtraescolar', models.CharField(max_length=50)),
                ('campusSegundo', models.CharField(max_length=10)),
            ],
        ),
    ]