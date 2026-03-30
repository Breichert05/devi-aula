import contextlib
import datetime
import io

from manage import *

saida = io.StringIO()
with contextlib.redirect_stdout(saida):
    main()

from relacionamentos.models import Pessoa, Revista, Passaporte, Reporter, Artigo
from django.core.exceptions import ValidationError


def criar_pessoa():
    try:
        print("=== Criando Pessoa ===")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        ano = int(input("Ano nascimento: "))
        mes = int(input("Mês nascimento: "))
        dia = int(input("Dia nascimento: "))

        pessoa = Pessoa(
            nome=nome,
            cpf=cpf,
            data_nascimento=datetime.date(ano, mes, dia)
        )

        pessoa.full_clean()
        pessoa.save()

        print(f"Pessoa criada com sucesso: {pessoa.nome}")

    except ValidationError as e:
        print("Erro ao criar pessoa:")
        print(e)


def criar_revista():
    try:
        print("=== Criando Revista ===")
        nome = input("Nome: ")
        edicao = int(input("Edição: "))

        revista = Revista(
            nome=nome,
            edicao=edicao
        )

        revista.full_clean()
        revista.save()

        print(f"Revista criada: {revista.nome} - {revista.edicao}")

    except ValidationError as e:
        print("Erro ao criar revista:")
        print(e)


def criar_passaporte():
    try:
        print("=== Criando Passaporte ===")
        pessoa_id = int(input("ID da Pessoa: "))
        numero = input("Número: ")

        pessoa = Pessoa.objects.get(id=pessoa_id)

        passaporte = Passaporte(
            numero=numero,
            emissao=datetime.date.today(),
            vencimento=datetime.date(2030, 1, 1),
            pessoa=pessoa
        )

        passaporte.full_clean()
        passaporte.save()

        print(f"Passaporte criado: {passaporte.numero} - {pessoa.nome}")

    except Pessoa.DoesNotExist:
        print("Pessoa não encontrada")

    except ValidationError as e:
        print("Erro ao criar passaporte:")
        print(e)


def criar_reporter():
    try:
        print("=== Criando Reporter ===")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        ano = int(input("Ano nascimento: "))
        mes = int(input("Mês nascimento: "))
        dia = int(input("Dia nascimento: "))
        email = input("Email: ")

        reporter = Reporter(
            nome=nome,
            cpf=cpf,
            data_nascimento=datetime.date(ano, mes, dia),
            email=email
        )

        reporter.full_clean()
        reporter.save()

        print(f"Reporter criado: {reporter.nome}")

    except Pessoa.DoesNotExist:
        print("Pessoa não encontrada")

    except ValidationError as e:
        print("Erro ao criar reporter:")
        print(e)


def criar_artigo():
    try:
        print("=== Criando Artigo ===")
        reporter_id = int(input("ID do Reporter: "))
        titulo = input("Título: ")

        reporter = Reporter.objects.get(id=reporter_id)

        artigo = Artigo(
            titulo=titulo,
            publicacao=datetime.date.today(),
            autor=reporter
        )

        artigo.full_clean()
        artigo.save()

        print(f"Artigo criado: {artigo.titulo}")

    except Reporter.DoesNotExist:
        print("Reporter não encontrado")

    except ValidationError as e:
        print("Erro ao criar artigo:")
        print(e)


def listar_pessoas():
    print("\n=== Pessoas ===")
    for p in Pessoa.objects.all():
        print(f"{p.id} - {p.nome} ({p.cpf})")


def listar_revistas():
    print("\n=== Revistas ===")
    for r in Revista.objects.all():
        print(f"{r.id} - {r.nome} - Edição {r.edicao}")


def listar_passaportes():
    print("\n=== Passaportes ===")
    for p in Passaporte.objects.all():
        print(f"{p.id} - {p.numero} - {p.pessoa.nome}")


def listar_reporters():
    print("\n=== Reporters ===")
    for r in Reporter.objects.all():
        print(f"{r.id} - {r.nome} ({r.email})")


def listar_artigos():
    print("\n=== Artigos ===")
    for a in Artigo.objects.all():
        print(f"{a.id} - {a.titulo} (Autor: {a.autor.nome})")


# =========================
# MENU
# =========================

def __main__():
    flag = True

    while flag:
        print("\n==== MENU ====")
        print("1. Criar Pessoa")
        print("2. Criar Revista")
        print("3. Criar Passaporte")
        print("4. Criar Reporter")
        print("5. Criar Artigo")
        print("6. Listar Pessoas")
        print("7. Listar Revistas")
        print("8. Listar Passaportes")
        print("9. Listar Reporters")
        print("10. Listar Artigos")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_pessoa()

        elif opcao == "2":
            criar_revista()

        elif opcao == "3":
            criar_passaporte()

        elif opcao == "4":
            criar_reporter()

        elif opcao == "5":
            criar_artigo()

        elif opcao == "6":
            listar_pessoas()

        elif opcao == "7":
            listar_revistas()

        elif opcao == "8":
            listar_passaportes()

        elif opcao == "9":
            listar_reporters()

        elif opcao == "10":
            listar_artigos()

        elif opcao == "0":
            print("Saindo...")
            flag = False

        else:
            print("Opção inválida!")

    print("Fim do script.")


if __name__ == "__main__":
    __main__()
