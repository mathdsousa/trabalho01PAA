# Universidade Federal de São Carlos
# Disciplina: Projeto e Análise de Algoritmos
# Turma: D
# Alunos: Matheus dos Santos Sousa
#         Nathália Brasilino Gimenes

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

    transforma = str(exponencialDC(base,n))

    print("{} {}".format(int(transforma[0]), len(transforma) - 1))

main()
