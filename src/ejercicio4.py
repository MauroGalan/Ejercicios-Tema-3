def imprime_pares_inverso(n):
    if n%2 == 0:
        numero = n
    else:
        numero = n-1
    for i in range(numero,1, -2):
        print(i, end=" ")

def imprime_inversow(n):
    if n%2 == 0:
        numero = n
    else:
        numero = n-1
    while numero >= 2:
        print(numero, end=" ")
        numero -= 2


imprime_pares_inverso(9)