import contextlib, io
import datetime

from manage import *

saida = io.StringIO()
with contextlib.redirect_stdout(saida):
    main()

from relacionamentos.models import Pessoa, Revista, Passaporte, Reporter, Artigo
from django.core.exceptions import ValidationError


def criar_dados():
    try:
        print("\n=== CRIANDO DADOS ===")

        pessoa1 = Pessoa(nome="Beatriz Macedo", data_nascimento=datetime.date(2005, 3, 5), cpf="12345678901")
        pessoa2 = Pessoa(nome="Ryan Engel", data_nascimento=datetime.date(2005, 2, 26), cpf="12345678159")
        pessoa3 = Pessoa(nome="Ana Sofia Reichert", data_nascimento=datetime.date(2015, 6, 21), cpf="12345015401")
        pessoa4 = Pessoa(nome="Janira Macedo", data_nascimento=datetime.date(1974, 1, 25), cpf="12345025901")
        pessoa5 = Pessoa(nome="Fabiano Peralta", data_nascimento=datetime.date(1975, 1, 21), cpf="54945678901")

        pessoas = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]

        for p in pessoas:
            p.full_clean()
            p.save()
            print(f"Pessoa criada: {p.nome}")

        revistas = [
            Revista(nome="Super Interessante", edicao=10),
            Revista(nome="Super Interessante", edicao=20),
            Revista(nome="Super Interessante", edicao=30),
            Revista(nome="Super Interessante", edicao=40),
            Revista(nome="Super Interessante", edicao=50),
        ]

        for r in revistas:
            r.full_clean()
            r.save()
            print(f"Revista criada: {r.nome} - {r.edicao}")

        passaportes = [
            Passaporte(numero="A1234567", emissao=datetime.date.today(), vencimento=datetime.date(2030, 1, 1),
                       pessoa=pessoa1),
            Passaporte(numero="B1234567", emissao=datetime.date.today(), vencimento=datetime.date(2030, 1, 1),
                       pessoa=pessoa2),
            Passaporte(numero="C1234567", emissao=datetime.date.today(), vencimento=datetime.date(2030, 1, 1),
                       pessoa=pessoa3),
            Passaporte(numero="D1234567", emissao=datetime.date.today(), vencimento=datetime.date(2030, 1, 1),
                       pessoa=pessoa4),
            Passaporte(numero="E1234567", emissao=datetime.date.today(), vencimento=datetime.date(2030, 1, 1),
                       pessoa=pessoa5),
        ]

        for p in passaportes:
            p.full_clean()
            p.save()
            print(f"Passaporte criado: {p.numero}")

        reporter1 = Reporter(
            nome="Carlos Silva",
            data_nascimento=datetime.date(1990, 5, 10),
            cpf="99911111111",
            email="carlos@gmail.com"
        )
        reporter2 = Reporter(
            nome="Fernanda Souza",
            data_nascimento=datetime.date(1988, 8, 22),
            cpf="99922222222",
            email="fernanda@gmail.com"
        )
        reporter3 = Reporter(
            nome="Lucas Pereira",
            data_nascimento=datetime.date(1995, 3, 15),
            cpf="99933333333",
            email="lucas@gmail.com"
        )
        reporter4 = Reporter(
            nome="Mariana Costa",
            data_nascimento=datetime.date(1992, 11, 30),
            cpf="99944444444",
            email="mariana@gmail.com"
        )
        reporter5 = Reporter(
            nome="João Santos",
            data_nascimento=datetime.date(1985, 7, 9),
            cpf="99955555555",
            email="joao@gmail.com"
        )

        reporters = [reporter1, reporter2, reporter3, reporter4, reporter5]

        for r in reporters:
            r.full_clean()
            r.save()
            print(f"Reporter criado: {r.nome}")

        artigos = [
            Artigo(titulo="Artigo 1", publicacao=datetime.date.today(), autor=reporter1),
            Artigo(titulo="Artigo 2", publicacao=datetime.date.today(), autor=reporter2),
            Artigo(titulo="Artigo 3", publicacao=datetime.date.today(), autor=reporter3),
            Artigo(titulo="Artigo 4", publicacao=datetime.date.today(), autor=reporter4),
            Artigo(titulo="Artigo 5", publicacao=datetime.date.today(), autor=reporter5),
        ]

        for a in artigos:
            a.full_clean()
            a.save()
            print(f"Artigo criado: {a.titulo}")

        print("\n=== DADOS CRIADOS COM SUCESSO ===")

    except ValidationError as e:
        print("\nErro durante criação:")
        print(e)


def deletar_dados():
    print("\n=== DELETANDO DADOS ===")

    Artigo.objects.all().delete()
    print("Artigos deletados")

    Reporter.objects.all().delete()
    print("Reporters deletados")

    Passaporte.objects.all().delete()
    print("Passaportes deletados")

    Revista.objects.all().delete()
    print("Revistas deletadas")

    Pessoa.objects.all().delete()
    print("Pessoas deletadas")

    print("\n=== BANCO LIMPO ===")


def __main__():
    while True:
        print("\n==== MENU ====")
        print("1. Criar dados")
        print("2. Deletar dados")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_dados()

        elif opcao == "2":
            deletar_dados()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    __main__()
