from modules.fileManager import loadCities, saveCities
from modules.ciudades import registrarCiudad, buscarCiudad, verCiudades

def menu():
    print("\n====== BIENVENIDO ======")
    print("1. Registrar ciudad")
    print("2. Ver ciudad por código")
    print("3. Ver todas las ciudades con sus códigos")
    print("0. Salir")
    opc = int(input("Ingrese la opción deseada: "))
    return opc

ciudades = loadCities()

opc = 10

while opc != 0:
    opc = menu()
    if opc == 1:
        print('Ciudad por código')
        ciudades = registrarCiudad(ciudades)
        saveCities(ciudades)

    elif opc == 2:
        print('Registrar ciudad')
        buscarCiudad(ciudades)

    elif opc == 3:
        print('Ver todas las ciudades con sus códigos')
        verCiudades(ciudades)

    elif opc == 0:
        print('Salir')
        exit()
    else:
        print('Opción incorrecta, revise y vuelva a intentar')