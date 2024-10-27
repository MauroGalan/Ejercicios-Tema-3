def calcula_precios (precio_normal, edades):
    precios_desc = []
    precio_red = precio_normal/2
    for edad in edades:
        if edad <= 18 or edad >= 65:
            precios_desc.append(precio_red)
        else:
            precios_desc.append(precio_normal)
    return precios_desc