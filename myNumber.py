"""
1. Validador de CPF Japonês (MyNumber simplificado)

Crie um programa que receba uma string representando um número de identificação (12 dígitos) e:

Verifique se contém apenas números.

Valide o comprimento (12 dígitos).

Retorne “Válido” ou “Inválido”.

💡 Desafio extra: implemente uma função que gera um número aleatório válido.
"""
from random import randint

def gerar_num_aleatorio(tamanho):    
    """Gera um número aleatório com a quantidade de dígitos especificada."""
    return "".join(str(randint(0,9)) for _ in range(tamanho))

def validar_mynumber(numero: str) -> bool:
    """Valida se o número tem apenas dígitos e exatamente 12 caracteres."""
    return numero.isdigit() and len(numero) == 12

def main():
    """Função principal do programa."""
    print("\n=== Menu MyNumber ===")
    print("[1] Gerar número aleatório")
    print("[2] Validar número")
    print("[3] Sair")
    opcao = input("Escolha uma opcao: ")
    match opcao:
        case "1":
            print("Seu novo numero de identidade:", gerar_num_aleatorio(12))
        case "2":
            my_number = input("Digite seu numero de identidade: ")

            if validar_mynumber(my_number):
                print("✅ Válido!")
            else:
                print("❌ Inválido! Deve conter apenas números e ter 12 dígitos.")
        case "3":
            print("Saindo...")
        case _:
            print("Opção inválida. Tente novamente.")
    
if __name__ == "__main__":
    main()
