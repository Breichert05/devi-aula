from datetime import date

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from relacionamentos.models import BaseModel, Reporter


class Artigo(BaseModel):
    titulo = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(5)],
        verbose_name="Título",
        help_text="Título do artigo"
    )

    publicacao = models.DateField(
        verbose_name="Data de Publicação",
        help_text="Selecione a data de publicação do artigo",
        validators=[MinValueValidator(date.today)]
    )
    # relacionamento 1:N
    autor = models.ForeignKey(
        Reporter,
        verbose_name="Reporter autor",
        help_text="Selecione o reporter autor do artigo",
        on_delete=models.CASCADE
    )

    def clean(self):
        data_publicacao = self.publicacao
        data_publicacao.replace(
            year=data_publicacao.year - 18
        )

        if self.autor.data_nascimento > data_publicacao:
            raise ValidationError({
                'publicacao': 'Reporter não possui idade mínima para publicar o artigo'
            })


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicacao', 'autor')
    search_fields = ('titulo', 'publicacao')
    list_filter = ('publicacao',)
