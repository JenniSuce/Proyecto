# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('calificaciones', models.CharField(max_length=5)),
                ('fecha_publicacion', models.DateField()),
                ('Alumno', models.ForeignKey(to='blog.Alumnos')),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombrecursos', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='Curso',
            field=models.ManyToManyField(to='blog.Cursos'),
        ),
    ]
