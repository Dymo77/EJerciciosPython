def llenarSec(n):
    x = 0
    tabla = []
    for i in range(n):
        tabla.append([])
        for j  in range(n):
            x += 1
            tabla[i]+= [x]
    return tabla

def imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print(" ]")

tabla = llenarSec(5)
imprimir(tabla)
