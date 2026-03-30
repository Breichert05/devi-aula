from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from exemplo.models import BaseModel
from exemplo.enumerations.pais import Pais
from exemplo.enumerations.profissao import Profissao

class Usuario(BaseModel):
    nome = models.CharField(validators=[MinLengthValidator(2)], max_length=50)
    sobrenome = models.CharField(validators=[MinLengthValidator(2)], max_length=100)
    nome_usuario = models.CharField(validators=[MinLengthValidator(3)], max_length=20, unique=True)
    pais = models.TextField(choices=Pais, default=Pais.OUTRO)
    email = models.EmailField()
    ranking = models.IntegerField(validators=[MinValueValidator(1)])
    profissao = models.TextField(choices=Profissao, default=Profissao.ESTUDANTE)
    sobre = models.TextField()
    instituicao = models.CharField(validators=[MinLengthValidator(3)], max_length=100)