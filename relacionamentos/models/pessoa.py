from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from relacionamentos.models import BaseModel
from relacionamentos.validators import valida_cpf


class Pessoa(BaseModel):
    nome = models.CharField(max_length=100,
                            help_text="Nome da pessoa",
                            validators=[MinLengthValidator(5)])
    data_nascimento = models.DateField(verbose_name="Data de Nascimento",
                                       help_text="Selecione a data de nascimento",
                                       validators=[])
    cpf = models.CharField(max_length=11, unique=True,
                           validators=[MinLengthValidator(11), valida_cpf],
                           help_text="Insira um CPF válido",
                           verbose_name="CPF")

    def clean(self):
        hoje = date.today()
        if self.data_nascimento > hoje:
            raise ValidationError({
                'data_nascimento': 'Não é possível inserir uma data de nascimento futura.'
            })
    def __str__(self):
        return self.nome