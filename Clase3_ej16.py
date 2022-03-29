import opcode
from random import randint

def ppt(op):
    if op == 1:
        r = "piedra"
    elif op == 2:
        r = "papel"
    elif op == 3: 
        r = "tijeras"
    return r


ganadas = 0
ganadasM=0

while (ganadas<3 or ganadasM<3):
    opUsuario = int(input("Ingrese una opcion: \n1.-Piedra\n2.-Papel\n3.-Tijeras\n"))
    if opUsuario>3 or opUsuario<1:
        continue
    opMaquina = randint(1,3)     
    print("El usuario escogio: ", ppt(opUsuario))
    print("La maquina escogio: ", ppt(opMaquina))
    if(opUsuario==1 and opMaquina==3) or (opUsuario==2 and opMaquina==1) or (opUsuario == 3 and opMaquina ==2):
        print("Gana el usuario!")
        ganadas += 1
    elif opUsuario == opMaquina:
        print("Empate!")
    else:
        ganadasM += 1
        print("gana la maquina")
    print("Usuario: ", ganadas)
    print("Maquina: ", ganadasM)

if ganadasM == 3:
    print("Gano la maquina")
    print("GG ez")
if ganadas == 3:
    print("Gano El usuario")
    print("GG ez")