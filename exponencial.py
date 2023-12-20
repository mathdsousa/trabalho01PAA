# Universidade Federal de São Carlos
# Disciplina: Projeto e Análise de Algoritmos
# Turma: D
# Alunos: Matheus dos Santos Sousa
#         Nathália Brasilino Gimenes

def exponencialDC(base, n):
    if n == 0:
        return 1
    if n == 1:
        return base
    metade = exponencialDC(base, n // 2)
    parcial = metade * metade
    if n % 2 == 1:
        return parcial * base
    return parcial

def main():
    # Entrada de valores
    i = 0

    while(i < 10):
        entrada = input()
        base, n = [int(numero) for numero in entrada.split(' ')]

        res = exponencialDC(base, n)

        # Calcular o logaritmo do resultado sem converter para string
        log = 0 if res == 0 else len(str(res))

        print("{} {}".format(res // 10**(log - 1), log - 1))
    
    i += 1

main()
