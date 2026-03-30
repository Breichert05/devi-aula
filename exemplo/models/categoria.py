from django.db import models
from exemplo.models import BaseModel


class Categoria(BaseModel):
    nome = models.CharField(max_length=20)
    area = models.CharField(max_length=20,
                            null=True, blank=True,
                            verbose_name="Área do conhecimento",
                            help_text="Informe a área do conhecimento segundo o padrão CAPES."
                            )
    instituicao = models.CharField(max_length=10,
                                   default="IFRS",
                                   verbose_name="Instituição",
                                   help_text="Digite a instituição com no máximo 10 caracteres."
                                   )

    def __str__(self):
        return f"{self.nome} - {self.area}/{self.instituicao}"
