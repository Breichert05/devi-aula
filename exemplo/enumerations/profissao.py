from django.db import models


class Profissao(models.TextChoices):
    # CONSTANTE = "NOME NO BD" , "NOME PARA USUARIO"
    ESTUDANTE = "Estudante", "Estudante"
    PROGRAMADOR = "Programador", "Programador"
    DESEMPREGADO = "Desempregado", "Desempregado"
    PROFESSOR = "Professor", "Professor"
    ANALISTA = ("Analista", "Analista de Sistemas")
