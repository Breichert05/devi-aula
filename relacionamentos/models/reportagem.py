from datetime import date

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from relacionamentos.models import BaseModel, Revista, Artigo, ArtigoAdmin


class Reportagem(BaseModel):
    titulo = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
        verbose_name="Título",
        help_text="TInsira o título da reportagem"
    )

    publicacao = models.DateField(
        verbose_name="Data de Publicação",
        validators=[MinValueValidator(date.today)],
        help_text="Selecione a data de publicação da reportagem"
    )

    # Field para o relacionamento N:N simples
    # O primeiro atributo é o modelo
    revistas = models.ManyToManyField(
        Revista,
        help_text="Selecione as revistas nas quais a reportagem foi publicada"
    )

    class Meta:
        verbose_name_plural = "Reportagens"
