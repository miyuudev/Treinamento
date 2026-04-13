"""
3️⃣ Maior de dois números

Peça dois números e diga qual é maior, ou se são iguais.
"""

def maior_numero(num1: int, num2: int) -> str:
    """Retorna uma mensagem indicando qual número é maior ou se são iguais."""
    if num1 == num2:
        return f"Os dois números são iguais: {num1}"
    else:
        maior = max(num1, num2)
        return f"O maior número é: {maior}"


def main():
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
        print(maior_numero(num1, num2))
    except ValueError:
        print("Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    main()
