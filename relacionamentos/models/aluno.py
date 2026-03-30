from tabnanny import verbose

from django.core.validators import EmailValidator, MinLengthValidator
from django.db import models

from relacionamentos.models import Pessoa, Disciplina

class Aluno(Pessoa):
    email = models.EmailField(verbose_name="E-mail",
                              help_text="E-mail institucional do aluno",
                              max_length=254
                              )
    cod = models.CharField(max_length=10,
                                 validators=[MinLengthValidator(10)],
                                 unique=True,
                                 verbose_name="Matricula",
                                 help_text="Digite a matrícula do aluno")
    disciplinas = models.ManyToManyField(Disciplina,
                                        through='Matricula',through_fields=('aluno', 'disciplina'),
                                        help_text="Selecione as disciplinas do aluno",
                                        )
    #todo: gerar numero de matricula automaticamente
    def __str__(self):
        return f"{self.cod} - {self.nome}"