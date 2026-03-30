from django.db import models


class Sexo(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMININO = 'F', 'Feminino'
    OUTRO = 'O', 'Outro'
