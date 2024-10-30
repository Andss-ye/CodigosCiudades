def menu():
    print("\n====== BIENVENIDO ======")
    print("1. Ver ciudad por código")
    print("2. Registrar ciudad")
    print("3. Ver todas las ciudades con sus códigos")
    print("4. Salir")
    opc = int(input("Ingrese la opción deseada: "))
    return opc

opc = 10
while opc != 0:
    opc = menu()
    if opc == 1:
        print('Ciudad por código')
    elif opc == 2:
        print('Registrar ciudad')
    elif opc == 3:
        print('Ver todas las ciudades con sus códigos')
    elif opc == 0:
        print('Salir')
        exit()
    else:
        print('Opción incorrecta, revise y vuelva a intentar')