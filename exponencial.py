# Universidade Federal de São Carlos
# Disciplina: Projeto e Análise de Algoritmos
# Turma: D
# Alunos: Matheus dos Santos Sousa
#         Nathália Brasilino Gimenes

def logaritmo(num):
    if (num >= 0 and num <= 9):
        return 0
    return 1 + logaritmo(num/10)

def exponencialDC(base, n):
    if n == 0:
        return 1
    metade = exponencialDC(base, n//2)
    parcial = metade * metade
    if(n % 2 == 1):
        return parcial * base
    return parcial

def main():
    # Entrada de valores
    entrada = input()
    base, n = [int(numero) for numero in entrada.split(' ')]

    res = exponencialDC(base, n)
    log = logaritmo(res)

    print("{} {}".format(res//10**log, log))

main()
