import random
def juego_adivina_numero(maximo):
    """
    1º Número aleatorio entre 1 y máximo
    2º Pedir número al jugador
    3º While Numero no es numero aleatorio
       Si el numero 
    Si el número es correcto se termina el juego
    """
    num_aleatorio = random.randint(1, maximo)
    num_jugador = None
    while num_aleatorio != num_jugador:
        num_jugador = int(input("Introduce un número: "))
        if num_jugador > num_aleatorio:
            print("Tu número", num_jugador, "es mayor")
        elif num_jugador < num_aleatorio:
            print("Tu número", num_jugador, "es menor")
    print("¡Correcto!, mi número era", num_aleatorio, ", y tu has acertado con", num_jugador)

juego_adivina_numero (8)