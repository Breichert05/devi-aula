from django.db import models


# enumerations -> variável choices -> opções para o usuário escolher
class Nivel(models.IntegerChoices):
    # CONSTANTE = "NOME NO BD" , "NOME PARA USUARIO"
    UM = 1, "Um"
    DOIS = 2, "Dois"
    TRES = 3, "Três"
    QUATRO = 4, "Quatro"
    CINCO = 5, "Cinco"
    SEIS = 6, "Seis"
    SETE = 7, "Sete"
    OITO = 8,  "Oito"
    NOVE = 9, "Nove"