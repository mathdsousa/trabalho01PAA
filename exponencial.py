# Cálculo do logaritmo
def logaritmo(num):
    if (num >= 0 and num <= 9):
        return 0
    return 1 + logaritmo(num/10)

# Cálculo do exponencial usando divisão e conquista
def exponencialDC(base, n):
    if n == 1:
        return base
    metade = n//2
    parcial = exponencialDC(base, metade)
    if(n % 2 == 0):
        return parcial * parcial
    return parcial * parcial * base

def main():
    # Entrada de valores
    base, n = int(input()), int(input())

    res = exponencialDC(base, n)
    log = logaritmo(res)

    print("{} {}".format(res//10**log, log))

main()
