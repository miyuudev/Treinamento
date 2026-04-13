"""
5️⃣ Validador de nota escolar

Receba uma nota (0–10).
Diga se o aluno foi aprovado (≥6), recuperação (4–5.9) ou reprovado (<4).
"""

def validacao(nota: float) -> str:
    if 6 <= nota <= 10:
        return f"{nota} → ✅ Aprovado!"
    elif 4 <= nota < 6:
        return f"{nota} → ⚠️ Recuperação!"
    elif 0 <= nota < 4:
        return f"{nota} → ❌ Reprovado!"
    else:
        return f"{nota} → 🚫 Nota inválida!"


def main():
    nota = float(input("Digite sua nota: "))
    print(validacao(nota))

if __name__ == "__main__":
    main()
