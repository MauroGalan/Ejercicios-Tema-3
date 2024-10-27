from collections import namedtuple
Persona = namedtuple("Persona", "nombre, edad")

def lee_personas(n):
    """
    Lee el nombre y la edad de n personas por teclado, 
    y devuelve una lista de tuplas de tipo Persona"""
    res= []
    for i in range(1,n+1):
        nombre = input(f"Diga el nombre de la persona {i}: ")
        edad = int(input(f"Diga la edad de {nombre}: "))
        res.append(Persona(nombre,edad))
    return res

personas = lee_personas(3)
print(personas)


def edad_media(personas):
    suma = 0
    for p in personas:
        suma += p.edad
    if len(personas) <= 0:
        return None
    else:
        return suma/len(personas)
    
def mayores_18(personas):
    mayores= []
    for p in personas:
        if p.edad >= 18:
            mayores.append(p.nombre)
    return sorted(mayores)

def edades_distintas(personas):
    edades = set()
    for p in personas:
        edades.add(p.edad)
    return sorted(edades)

def persona_mas_joven(personas):
    min = None
    for p in personas:
        if min == None or p.edad < min.edad:
            min = p
    if min == None:
        return None
    else:
       return min.nombre
