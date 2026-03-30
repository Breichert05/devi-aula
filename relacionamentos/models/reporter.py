from django.core.validators import MinLengthValidator
from django.db import models

from relacionamentos.models import Pessoa


class Reporter(Pessoa):
    email = models.EmailField(
        max_length=100,
        validators=[MinLengthValidator(5)],
        verbose_name="Email",
        help_text="Insira o e-mail institucional"
    )

