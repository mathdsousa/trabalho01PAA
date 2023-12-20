# Universidade Federal de São Carlos
# Disciplina: Projeto e Análise de Algoritmos
# Turma: D
# Alunos: Matheus dos Santos Sousa
#         Nathália Brasilino Gimenes

#Conquista, juntamente com a contagem das inversões
def intercalaContando(genoma2, inicio, metade, fim, pesos):
    
    num_inv = 0
    i = inicio
    j = metade
    k = 0
    tam = fim - inicio
    w = [None] * tam

    while(i < metade and j < fim):
        #Aqui fazemos a comparação utilizando a lista de pesos
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

#Processo de divisão do problema e soma das inversões
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

#Para entrada do genoma 1, criamos em paralelo uma lista de pesos, na qual armazena-se em cada índice
#a posição do valor do índice em relação ao genoma 1
#EX: genoma 1: caso o gene 3 esteja na posição 1, então na posição 3 da lista de peso, armazenamos o valor 1
#Esta lista de peso utilizaremos para fazer a comparação entre os genes do genoma 2
def preencheLista(num, bool):
    entrada = input().strip()
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
    #entradas dos genomas 1 e 2, e criação de uma lista de pesos
    genoma1, pesos = preencheLista(num, True)
    genoma2 = preencheLista(num, False)

    num_inv = contarInversoes(genoma2, num, pesos)
    print(num_inv)

main()
