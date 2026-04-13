"""
1️⃣ Verificador de idade

Peça a idade e diga se a pessoa é: criança (0–12), adolescente (13–17),
adulto (18–59) ou idoso (60+).
"""

def verificar_idade(idade:int) -> str:
    """indica que mesmo entrando um num inteiro vai retornar uma str"""
    if idade <= 12:
        return "crianca"
    elif 13 <= idade <= 17:
        return "adolescente"
    elif idade > 17:
        return "adulto"
    else:
        return "idade invalida"


def main():
    """"""
    try:
        idade = int(input("Digite a sua idade: "))
        print(verificar_idade(idade))
    except ValueError:
        print("Por favor, digite um número válido.")


if __name__ == "__main__":
    main()
