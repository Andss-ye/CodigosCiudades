def validacionCodigoRepetido(codigo, ciudades):
    if codigo in ciudades:
        return -1
    else:
        return codigo