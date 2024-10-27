def fecha_en_intervalo (fecha_min,fecha_max,fecha):
    if (fecha_min == None or fecha >= fecha_min) and\
    (fecha_max == None or fecha <= fecha_max):
        return True
    else:
        return False

#return (fecha_min == None or fecha >= fecha_min) and\
    (fecha_max == None or fecha <= fecha_max)
