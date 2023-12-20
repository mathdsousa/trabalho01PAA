# Universidade Federal de São Carlos
# Disciplina: Projeto e Análise de Algoritmos
# Turma: D
# Alunos: Matheus dos Santos Sousa
#         Nathália Brasilino Gimenes

def intercalaContando(genoma2, inicio, metade, fim, pesos):
    
    num_inv = 0
    i = inicio
    j = metade
    k = 0
    tam = fim - inicio
    w = [None] * tam

    while(i < metade and j < fim):
        if(pesos[genoma2[i]] <= pesos[genoma2[j]]):
            w[k] = genoma2[i]
            k += 1
            i += 1
        else:
            w[k] = genoma2[j]
            k += 1
            j += 1
            num_inv += metade - i

    while(i < metade):
        w[k] = genoma2[i]
        k += 1
        i += 1

    while(j < fim):
        w[k] = genoma2[j]
        k += 1
        j += 1

    k = 0

    for k in range(tam):
        genoma2[inicio + k] = w[k]
    
    return num_inv

def contarInversoesR(genoma2, inicio, fim, pesos):
    numInversoes = 0
    if(fim - inicio > 1):
        metade = (inicio + fim) // 2
        numInversoes += contarInversoesR(genoma2, inicio, metade, pesos)
        numInversoes += contarInversoesR(genoma2, metade, fim, pesos)
        numInversoes += intercalaContando(genoma2, inicio, metade, fim, pesos)
    return numInversoes

def contarInversoes(genoma2, n, pesos):
    return contarInversoesR(genoma2, 0, n, pesos)

def preencheLista(num, bool):
    entrada = input()
    lista1 = [int(numero) for numero in entrada.split(' ')]
    if bool:
        lista2 = [0] * num
        for i in range(num):
            a = lista1[i]
            lista2[a] = i
        return lista1, lista2
    return lista1


def main():
    num = int(input())

    genoma1, pesos = preencheLista(num, True)
    genoma2 = preencheLista(num, False)
    #print(genoma1)
    #print(pesos)
    #print(genoma2)

    num_inv = contarInversoes(genoma2, num, pesos)
    
    #print(genoma2)
    print(num_inv)

main()
