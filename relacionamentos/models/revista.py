from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from relacionamentos.models import BaseModel


class Revista(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        help_text="Nome da revista"
    )

    edicao = models.IntegerField(
        verbose_name="Edição",
        help_text="Edição da revista",
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('nome', 'edicao')

    def __str__(self):
        return f"{self.nome} - Edição {self.edicao}"