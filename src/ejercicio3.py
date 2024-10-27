def imprime_pares(n):
    numero = 2
    while numero <= n:
        print(numero, end=" ")
        numero += 2
    for i in range(1,n+1):
        if i%2 == 0:
            print(i, end=" ")

Defina una función imprime_pares que reciba un entero n e imprima en la consola los números pares positivos menores o iguales a n. Todos los números se deben imprimir en una sola línea, separados por espacios.