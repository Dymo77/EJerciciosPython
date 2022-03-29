from cgi import print_directory
from random import randint 

#randrange numero aleatorio entero entre "x" y  "y" con paso de p
#uniform numero aleatorio de tipo float entre "x" y "y"

zUs = int(input("En que zona desea disparar? "))
zoP = randint(1 , 6)

print("La zona cubierta por el portero fue: " , zoP)

if zUs == zoP:
    print("No ha sido gol")
else:
    print("Golazooo")