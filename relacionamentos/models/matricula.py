from django.core.validators import MinValueValidator, MaxValueValidator

from relacionamentos.enumerations import Status
from relacionamentos.models import BaseModel, Aluno, Disciplina
from django.db import models


class Matricula(BaseModel):
    data = models.DateField(help_text="Insira a data da matricula")
    nota = models.FloatField(help_text="Nota final do aluno",
                             validators=[MinValueValidator(0.0), MaxValueValidator(10,0)])
    frequencia = models.FloatField(verbose_name= "Frequência",
                            help_text="Informa a frequencia final do aluno")
    status = models.CharField(max_length=20,
                              help_text="Status do aluno para a matricula",
                              default= Status.MATRICULADO,
                              choices=Status)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, help_text= "Selecione o aluno para a matricula",  )

    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, help_text= "Selecione o disciplina para o aluno", )

    def __str__(self):
        return f"{self.data} - {self.aluno.nome} - {self.disciplina.nome}"
    #salvar data atual
    #verificar o status de acordo com a nota e frequencia