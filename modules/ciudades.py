from modules.validaciones import validacionCodigoRepetido

def registrarCiudad(ciudades):
    codigo = validacionCodigoRepetido(str(input('\nIngrese el codigo de la ciudad a registrar: ')).upper(), ciudades)
    ciudad = str(input('\nIngrese el nombre de la ciudad: ')).upper()

    if codigo == '':
        print('\nEl codigo a registrar no tiene que ser vacio')
        return ciudades

    if codigo != -1:
        ciudades[codigo] = ciudad
        print(f'\nCiudad registrada con codigo {codigo} y nombre {ciudad}'.format(codigo=codigo, ciudad=ciudad))
        return ciudades
    else:
        print('\nEl codigo ingresado ya existe en la base de datos de ciudades, verifique antes.')
        return ciudades

def buscarCiudad(ciudades):
    codigo = str(input('\nIngrese el codigo de la ciudad a buscar: ')).upper()

    if codigo == '':
        print('\nEl codigo a buscar no puede ser vacio')
        return 

    ciudad = ciudades.get(codigo)

    if ciudad:
        print(f'\nCiudad encontrada con codigo {codigo} y nombre {ciudad}'.format(codigo=codigo, ciudad=ciudad))
    else:
        print(f'\nCiudad no encontrada con codigo {codigo}'.format(codigo=codigo))
    
    return 

def verCiudades(ciudades):
    print('\nCiudades registradas: ')
    
    if ciudades:
        for ciudad in ciudades:
            print(f'codigo: {ciudad} ciudad: {ciudades[ciudad]}')
    else:
        print('No hay ciudades registradas')
    
    return