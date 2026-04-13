"""
4️⃣ Senha secreta

Peça uma senha e valide se é igual a "python123".
Mostre mensagens adequadas para certo e errado.
"""

def validacao(senha:str) -> bool:
    dado = "python123"
    return dado == senha

def main():
    senha = input("Digite uma senha: ").strip()
    if validacao(senha):
        print("✅ Acesso permitido!")
    else:
        print("❌ Senha incorreta. Tente novamente.")

if __name__ == "__main__":
    main()
