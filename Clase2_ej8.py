jornada = 48
hTrabajadas = int(input("ingrese las horas trabjadas. "))
pagoH = 2
pagoHex = 3.5

if hTrabajadas <= jornada:
    salario = hTrabajadas*pagoH
else:
    salario = (jornada*pagoH) + ((hTrabajadas-jornada)*pagoHex)

print("Su pago total es de: ", salario)