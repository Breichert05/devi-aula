from django.db import models


class Pais(models.TextChoices):
    # CONSTANTE = "NOME NO BD" , "NOME PARA USUARIO"
    BRASIL = "BR", "BRASIL"
    EUA = "EUA", "Estados Unidos"
    IRA = "IRA", "Irã"
    ARGENTINA = "ARG", "Argentina"
    OUTRO = "OUT", "Outro"