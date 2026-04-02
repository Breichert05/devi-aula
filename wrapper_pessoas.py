from decimal import Decimal

from django.core.exceptions import ValidationError

from manage import *
import contextlib, io

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()

from exemplo.models import Esporte, Time, Cidade, Pessoa
from exemplo.enumerations import Sexo

processados = 0
erros = 0

## Lê o arquivo CSV
with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    try:
        ## pega a primeira linha do arquivo e lê
        ## vamos apenas ler a primeira linha do arquivo, pois ela contém os nomes das colunas e queremos ignorá-la
        arquivo.readline()
        for linha in arquivo:
            dados = linha.split(',')
            nome = dados[0]
            sexo = dados[1]
            idade = int(dados[2])
            cidade = dados[3]
            estado = dados[4]
            time = dados[5]
            renda = Decimal(dados[6])
            esporte = dados[7]

            if sexo.upper() == 'MASCULINO':
                sexo = Sexo.MASCULINO

            elif sexo.upper() == 'FEMININO':
                sexo = Sexo.FEMININO

            else:
                raise ValueError('Sexo não cadastrado no ENUM')

            try:
                ## objects é o manager da classe
                ## filter retorna um QuerySet (não guarda objetos repetidos)
                endereco = Cidade.objects.filter(nome=cidade, estado=estado)

                ## cidade não está cadastrada
                if len(endereco) == 0:
                    try:
                        cidade_cadastrada = Cidade(nome=cidade, estado=estado)
                        cidade_cadastrada.full_clean()
                        cidade_cadastrada.save()
                    except ValidationError as e:
                        print(e)
                ## cidade cadastrada
                elif len(endereco) == 1:
                    cidade_cadastrada = endereco[0]
                else:
                    raise ValueError('Cidade em duplicidade')
            except Exception as e:
                print(e)
                print("Erro endereço")

            try:
                clube = Time.objects.filter(nome=time)

                ## time não cadastrado
                if len(clube) == 0:
                    time_favorito = Time(nome=time)
                    time_favorito.full_clean()
                    time_favorito.save()
                ## time cadastrado
                elif len(clube) == 1:
                    time_favorito = clube[0]
                else:
                    raise ValueError('Clube em duplicidade')
            except Exception as e:
                print(e)
                print("Erro time")

            try:
                esporte_cadastrado = Esporte.objects.filter(nome=esporte)

                ## esporte não cadastrado
                if len(esporte_cadastrado) == 0:
                    esporte_favorito = Esporte(nome=esporte)
                    esporte_favorito.full_clean()
                    esporte_favorito.save()
                ## esporte cadastrado
                elif len(esporte_cadastrado) == 1:
                    esporte_favorito = esporte_cadastrado[0]
                else:
                    raise ValueError('Esporte em duplicidade')
            except Exception as e:
                print(e)
                print("Erro esporte")

            try:
                nova_pessoa = Pessoa(
                    nome=nome,
                    idade=idade,
                    renda=renda,
                    time=time_favorito,
                    cidade=cidade_cadastrada,
                    esporte=esporte_favorito,
                    sexo=sexo
                )

                nova_pessoa.full_clean()
                nova_pessoa.save()
                print(f'Registro processado: {linha}')
                processados += 1
            except Exception as e:
                print(e)
                erros += 1
                print("Erro ao criar pessoa")
    except Exception as e:
        print(f'Problema ao salvar: {linha}')
        print(e)
        erros += 1

print("Processamento concluído")
print(f"Registros processados: {processados}")
print("Registros corretamente processados:")
print(f"Registros com erros: {erros}")
