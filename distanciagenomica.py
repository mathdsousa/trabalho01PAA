def interContando():
    pass

def contarInversoes(genoma2, inicio, fim, pesos):
    numInversoes = 0
    if(inicio - fim > 1):
        metade = (inicio + fim // 2)
        numInversoes += contarInversoes(genoma2, inicio, metade, pesos)
        numInversoes += contarInversoes(genoma2, metade, fim, pesos)
        numInversoes += interContando()
    return numInversoes



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
    print(genoma1)
    print(pesos)
    print(genoma2)

main()
