from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from exemplo.enumerations import Sexo
from exemplo.models import BaseModel
from exemplo.models import Time
from exemplo.models import Cidade
from exemplo.models import Esporte

class Pessoa(BaseModel):
    nome = models.CharField(validators=[MinLengthValidator(3)], max_length=40)
    nascimento = models.DateField()
    cpf = models.CharField(validators=[MinLengthValidator(11)], max_length=11, unique=True)

    responsavel = models.CharField(max_length=100)
    idade = models.IntegerField(
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(200)
        ],
    )

    renda = models.DecimalField(decimal_places=2, max_digits=10)

    time = models.ForeignKey(Time, on_delete=models.RESTRICT)

    cidade = models.ForeignKey(Cidade, on_delete=models.RESTRICT)

    esporte = models.ForeignKey(Esporte, on_delete=models.RESTRICT)

    sexo = models.TextField(
        choices=Sexo
    )

    def clean(self):
        hoje = date.today()
        limite = hoje.replace(year=hoje.year - 18)

        if self.nascimento > hoje:
            raise ValidationError({
                "nascimento": "A data de nascimento não pode ser no futuro."
            })

        if self.nascimento > limite and not self.responsavel:
            raise ValidationError({
                "responsavel": "Este campo é obrigatório para pessoas menores de 18 anos."
            })
