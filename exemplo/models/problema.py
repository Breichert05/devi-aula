from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models
from exemplo.models import BaseModel
from exemplo.enumerations.nivel import Nivel
from exemplo.validators.memory_validator import validar_tamanho_memoria
from exemplo.validators.palavras_proibidas import PalavrasProibidas


class Problema(BaseModel):
    cod = models.IntegerField(unique=True,
                              validators=[MinValueValidator(1000), ],
                              help_text='Codigo do problema'
                              )
    titulo = models.CharField(max_length=100,
                              validators=[MinLengthValidator(3), PalavrasProibidas(lista_proibida=["teste", "admin", ],
                                                                                   mensagem="O campo contém palavras "
                                                                                            "que foram proibidas. Ex: "
                                                                                            "teste, admin")],
                              help_text='Titulo do problema',
                              verbose_name='Titulo'
                              )
    nivel = models.IntegerField(choices=Nivel, default=Nivel.UM,
                                verbose_name='Nivel',
                                help_text='Escolha o nivel do problema')
    descricao = models.TextField(max_length=2000,
                                 validators=[MinLengthValidator(20),
                                             PalavrasProibidas(lista_proibida=["irã", "trump", "eua"],
                                                               mensagem="O campo contém "
                                                                        "palavras que "
                                                                        "foram proibidas. "
                                                                        "Revise as "
                                                                        "diretrizes")],
                                 verbose_name='Descrição',
                                 help_text="Insira a descrição do problema para o usuário"
                                 )
    exemplo_entrada = models.TextField(max_length=2000,
                                       verbose_name='Exemplo de entrada',
                                       help_text='Entrada para a solução do problema',
                                       )
    exemplo_saida = models.TextField(max_length=2000,
                                     validators=[MinLengthValidator(1), ],
                                     verbose_name="Exemplo de saida",
                                     help_text='Saida esperada para a solução do problema',
                                     )
    testes_entrada = models.TextField(max_length=2000,
                                      verbose_name='Exemplo de entrada',
                                      help_text='Entrada para a solução do problema',
                                      )
    testes_saida = models.TextField(max_length=2000,
                                    validators=[MinLengthValidator(1), ],
                                    verbose_name="Exemplo de saida",
                                    help_text='Saida esperada para a solução do problema',
                                    )
    pontuacao = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
                                  verbose_name="Pontuação",
                                  help_text="Insira a pontuação a ser creditada para o usuario")
    tempo_execucao = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)],
                                         verbose_name="Tempo de execucao do programa",
                                         help_text="Insira o tempo maximo de execução do programa", )
    memoria_maxima = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(256), validar_tamanho_memoria],
        verbose_name="Memoria maxima",
        help_text="Informe a quantidade maxima em MB de memoria maxima a ser "
                  "utilizada", )
    resolvidos = models.IntegerField(validators=[MinValueValidator(0)],
                                     verbose_name="Resolvidos",
                                     default=0,
                                     help_text="Quantidade de usuarios que resolveram o problema", )

    def clean(self):
        if self.pontuacao > 0  and self.resolvidos > 0:
            raise ValidationError(
                {
                    'pontuacao': "Pontuação não pode ser maior que zero, no caso de resolvidos maior que zero",
                    'resolvidos': "Não pode haver pessoas que resolveram o problema se a pontuação é maior que zero."
                }
            )
        elif "teste" in self.descricao and "teste" in self.exemplo_entrada:
            raise ValidationError(
                {
                    'descricao': "No caso de teste, apenas um campo pode conter a palavra teste",
                    'exemplo_entrada': "No caso de teste, apenas um campo pode conter a palavra teste"
                }
            )

    class Meta:
        unique_together = ('titulo', 'nivel')
        verbose_name = 'Problema de Computação'
        verbose_name_plural = 'Problemas de Computação'
        ordering = ['titulo'] # colocar - na frente para explicitar que a ordem é DESC, exemplo: -titulo

    def __str__(self):
        return f"{self.cod} - {self.titulo}"

    # bloquear o resolvidos de alteração

    # Existem 4 tipos de validadore que podemos usar:
    # 1 validador nativo = unique, notnull
    # 2 validador que já existem no django = MinValueValidator - chamado antes de salvar um objeto
    # 3 validadores customizados ou criados pelo usuario, mas tbm vai dentro ddo "validator"
    # 4 validador crossfiled, um campo dependente de outro campo
