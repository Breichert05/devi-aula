from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from relacionamentos.models import BaseModel, Pessoa


class Passaporte(BaseModel):
    numero = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(4)],
        verbose_name="Número do Passaporte",
        help_text="Digite o número do passaporte"
    )

    emissao = models.DateField(
        verbose_name="Data de Emissão",
        help_text="Selecione a data de emissão do passaporte",
        validators=[MinValueValidator(date.today),
                    MaxValueValidator(date.today)]
    )

    vencimento = models.DateField(
        verbose_name="Data de Vencimento do Passaporte",
        help_text="Selecione a data de vencimento do passaporte",
    )

    pessoa = models.OneToOneField(
        Pessoa,
        help_text="Selecione o titular do passaporte",
        on_delete=models.CASCADE
    )

    def clean(self):
        if self.emissao > self.vencimento:
            raise ValidationError({
                'emissao': 'Data de emissão não pode ser posterior à data de vencimento.',
                'vencimento': 'Data de vencimento não pode ser anterior à data de emissão.'
            })
        if self.pessoa.data_nascimento > self.emissao:
            raise ValidationError({
                'emissao': 'Data de emissão não pode ser anterior à data de nascimento do titular'
            })
