saldo = 0
op = 0

while(op != 3):
    op = int(input("Ingrese una opcion:\n1.-Deposito\n2.-Recargar\n3.-Salir\n"))
    if op == 1:
        cant = float(input("Ingrese una cantidad: "))
        saldo+=cant
    elif op == 2:
        cant = float(input("Ingrese cantidad: "))
        if cant > saldo:
            print("Saldo insuficiente")
        else: 
            saldo -= cant
    elif op == 3: 
        print("Saliendo...")
print ("Su saldo total es de: ", str(saldo))