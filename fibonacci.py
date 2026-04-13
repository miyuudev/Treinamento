"""
Fomula basica de Fibinacci
seq[n] = seq[n-1] + seq[n-2]
"""

def fibonacci(n:int):
    """Com o inicio e fim do range, o looping cria a l
    ista de sequencia ate chegar ao enesimo termo"""
    seq = [0, 1]
    for i in range(2, n+1):
        seq.append(seq[i-1]+seq[i-2])
    return seq[n], seq


def main():
    """O usuario fornece o enesimo termo da sequencia"""
    try:
        n = int(input("Escolha um termo da sequencia de fibonacci: "))
        termo, lista = fibonacci(n)
        print(f"O enésimo termo é: {termo}")
        print(f"Sequência até esse termo: {lista[1:]}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

if __name__ =="__main__":
    main()
