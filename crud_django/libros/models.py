from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 255)
    apaterno = models.CharField(max_length = 255)
    amaterno = models.CharField(max_length = 255)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 255)
    editorial = models.CharField(max_length = 255)
    no_paginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre