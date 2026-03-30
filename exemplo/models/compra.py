from django.core.validators import MinLengthValidator
from django.db import models
from exemplo.models import BaseModel


class Compra(BaseModel):
    data = models.DateField()
    hora = models.TimeField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    peso = models.FloatField
    descricao = models.TextField()
    cliente = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11,
                           validators=[MinLengthValidator(10)]
                           )
    def __str__(self):
        return f"Compra de {self.valor} realizada por {self.cliente} no dia {self.data} às {self.hora}"
