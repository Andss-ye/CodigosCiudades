def registrarCiudad(ciudades):
    codigo = str(input('\nIngrese el código de la ciudad a registrar: ')).upper()
    ciudad = str(input('\nIngrese el nombre de la ciudad: ')).upper()
    ciudades[codigo] = ciudad
    
    print(f'\nCiudad registrada con codigo {codigo} y nombre {ciudad}'.format(codigo=codigo, ciudad=ciudad))

    return ciudades