d = int(input("Ingrese la cantidad de dias "))
a = d//365
m = (d % 365)//30
s = (d - (a*365+m*30))//7
d2 = d - (a*365 + m*30+s*7)
print(d, "dias equivalen a: ", a ,"años, ", m ,"meses, ", s ,"semanas, " , d2, "dias ")
