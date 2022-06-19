from distutils.command.upload import upload
from enum import auto
from msilib.schema import Upgrade
from os import link
from tabnanny import verbose
from turtle import update
from unicodedata import name
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to= "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    update = models.TimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]

    def __str__(self):
        return self.title
        