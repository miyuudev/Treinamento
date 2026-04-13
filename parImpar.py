"""
2️⃣ Par ou ímpar

Receba um número e diga se é par ou ímpar.
"""
def is_par(numero:int) -> bool:
    """Verifica se o numero e par"""
    return  numero % 2 == 0

def main():
    numero = int(input("Digite um numero: "))
    resultado = "par" if is_par(numero) else "ímpar"
    print(f"O número {numero} é {resultado}.")


if __name__ == "__main__":
    main()
