# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-02 02:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=20)),
                ('ruc', models.IntegerField(blank=True)),
                ('auditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Banco.Auditor')),
            ],
        ),
        migrations.CreateModel(
            name='Egresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egresos', models.FloatField()),
                ('porcentaje', models.FloatField()),
                ('egresos_neto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresos', models.FloatField()),
                ('porcentaje', models.FloatField()),
                ('ingresos_neto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=50)),
                ('universidad', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('año_egreso', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='banco',
            name='fk_egresos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Banco.Egresos'),
        ),
        migrations.AddField(
            model_name='banco',
            name='fk_ingresos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Banco.Ingresos'),
        ),
        migrations.AddField(
            model_name='banco',
            name='fk_personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Banco.Personal'),
        ),
        migrations.AddField(
            model_name='banco',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
