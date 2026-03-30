from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from relacionamentos.models import BaseModel


class Disciplina(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5)],
                            help_text="Nome da disciplina"
                            )
    sigla = models.CharField(max_length=5,
                             validators=[MinLengthValidator(3)],
                             help_text="Sigla da disciplina")
    semestre = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(10)],
                                   help_text="Semestre da disciplina")
    ementa = models.TextField(help_text="Ementa da disciplina")

    def __str__(self):
        return self.nome