from django.core.validators import MinLengthValidator
from django.db import models

from exemplo.models import BaseModel


class Esporte(BaseModel):
    nome = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(4)]
    )

    def __str__(self):
        return self.nome
