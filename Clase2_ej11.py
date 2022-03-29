aIni = 2000
aFin = 2022
r = "Lo anios bisiestos entre "+ str(aIni) + " y " + str(aFin) + " son: "
for i in range(aIni,aFin):
    if (i%4==0 and i%100!=0) or i%400==0 : 
        r = r+ str(i)+ ","
print(r)