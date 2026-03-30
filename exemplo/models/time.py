from django.core import validators
from django.db import models

from exemplo.models import BaseModel


class Time(BaseModel):
    nome = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(3)],
    )

    def __str__(self):
        return self.nome