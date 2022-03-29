rcor = int(input("Ingrese las respuestas correctas: "))
rinc = int(input("Ingrese las respuestas incorrectas : "))
sum = rcor + rinc 
pc= (100/sum)*rcor
pi = (100/sum)*rinc
nota = rcor // sum 
print("La nota obtenida es: "+str(rcor)+"/" + str(sum))
print("El porcentaje de aciertos es : %.2f y un porcentaje de errores de %.2f"%(pc,pi))