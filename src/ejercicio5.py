def indica_primer_aparicion(lista,valor):
    posicion = -1
    for i, elem in enumerate(lista):
        if elem == valor:
            posicion = i
            break
    return posicion