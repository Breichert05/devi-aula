# validador usando classes - recebe parâmetros
# @ decorator
from xml.dom import VALIDATION_ERR

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# Permite que os objetos dessa classe sejam serializados e deserializados
# O django pode contruir e destruir objetos dessa classe
@deconstructible
class PalavrasProibidas:

    # Como instanciar os objetos dessa classe
    def __init__(self, lista_proibida: list, mensagem: str):
        if not isinstance(lista_proibida, list):
            raise TypeError("Lista proibida deve ser do tipo list")
        elif len(lista_proibida) == 0:
            raise ValueError("A lista de palavras não deve ser vazia")
        elif not isinstance(mensagem, str):
            raise TypeError("A mensagem deve ser do tipo string")
        elif mensagem.strip() == "":
            raise ValueError("A mensagem para o usuario não deve ser vazia")
        self.lista_proibida = lista_proibida
        self.mensagem = mensagem

    # O que será executado quando for invocado
    def __call__(self, valor_campo):
        for palavra in self.lista_proibida:
            if palavra.lower() in valor_campo.lower():
                raise ValidationError(
                    self.mensagem,
                    params={"value": valor_campo},
                )

    # Como determinar se o objeto é igual a outro
    def __eq__(self, outro):
        if isinstance(outro, PalavrasProibidas):  # mesmo tipo
            if len(self.lista_proibida) == len(outro.lista_proibida):  # mesmo tamanho
                for palavra in self.lista_proibida:  # se não conter uma determinada palavra
                    if palavra not in outro.lista_proibida:  # independente da ordem
                        return False
                # mesmo tipo, mesmo tamanho, mesmas palavras
                return True
        return False
