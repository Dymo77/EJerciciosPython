lista = [1,"hola",3.5,False]

while len(lista) > 0: 
    print(lista)
    elem = int(input("Ingrese la posición del elemento a elminiar: \n"))
    if elem>len(lista)-1:
        print("El elemento esta fuera del rango")
        continue
    del(lista[elem])
    print()
    