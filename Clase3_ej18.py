from random import randint 

v = True
aciertos = 0
while v: 
    op = randint(1,10)
    num1 = randint(1,10)
    num2 = randint(1,10)
    if op == 1:
        res = num1*num2
        print(num1, " x ",num2," = ")
        resUsuario = int(input("Ingrese su respuesta "))
        if resUsuario == res: 
            print("Correcto")
            aciertos += 1
        else:
            print("Incorrecto")
            v = False 
    if op == 2:
        res = num1//num2
        print(num1, " / ",num2," = ")
        resUsuario = int(input("Ingrese su respuesta "))
        if resUsuario == res: 
            print("Correcto")
            aciertos += 1
        else:
            print("Incorrecto, la respuesta era: ", res)
            v = False 

print("Tuvo un total de ", aciertos, " respuestas correctas")