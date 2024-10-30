def registrarCiudad(ciudades):
    codigo = str(input('\nIngrese el código de la ciudad a registrar: ')).upper()
    ciudad = str(input('\nIngrese el nombre de la ciudad: ')).upper()
    ciudades[codigo] = ciudad
    
    print(f'\nCiudad registrada con codigo {codigo} y nombre {ciudad}'.format(codigo=codigo, ciudad=ciudad))

    return ciudades

def buscarCiudad(ciudades):
    codigo = str(input('\nIngrese el código de la ciudad a buscar: ')).upper()
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