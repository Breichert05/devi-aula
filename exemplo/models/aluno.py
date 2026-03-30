from django.db import models
from exemplo.models import BaseModel


class Aluno(BaseModel):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    matricula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.matricula}"