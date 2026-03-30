from django.db import models

class Status(models.TextChoices):
    #CONSTANTE = NOME_DB, NOME_USUARIO
    APROVADO = "Aprovado","Aprovado"
    APROVADO_EM_EXAME = "Aprovado em exame","Aprovado em exame"
    EM_EXAME = "Em Exame","Em Exame"
    MATRICULADO = "Matriculado","Matriculado"
    REPROVADO = "Reprovado", "Reprovado"
    TRANCADO = "Trancado","Trancado"