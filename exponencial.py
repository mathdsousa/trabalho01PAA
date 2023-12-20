# Universidade Federal de São Carlos
# Disciplina: Projeto e Análise de Algoritmos
# Turma: D
# Alunos: Matheus dos Santos Sousa
#         Nathália Brasilino Gimenes

# Universidade Federal de São Carlos
# Disciplina: Projeto e Análise de Algoritmos
# Turma: D
# Alunos: Matheus dos Santos Sousa
#         Nathália Brasilino Gimenes


def exponencial(a, n):
    if (n == 0):
        return 1
    half = exponencial(a, n//2)
    res = half * half
    if(n % 2 == 1):
        return res * a
    return res 
    
def main():
    
    entrada = input()
    aux = entrada.split(' ')
    base, n = float(aux[0]), int(aux[1])
    
    res = str(int(exponencial(base, n)))
    
    print(res)
    
    print("{} {}".format(int(res[0]), len(res) - 1))
    
main()
    