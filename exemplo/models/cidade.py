from django.core.validators import MinLengthValidator
from django.db import models

from exemplo.models import BaseModel


class Cidade(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )

    estado = models.CharField(
        max_length=2,
        validators=[MinLengthValidator(2)]
    )

    def __str__(self):
        return f"{self.nome} - {self.estado}"