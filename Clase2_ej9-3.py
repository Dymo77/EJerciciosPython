h = 23
min = 45
seg = 45

if h <=23 and min <=59 and seg <=59:
    seg += 1
    if seg < 59:
        seg = 0
        min+=1
    if min > 59:
        min = 0
        h+1
    if h >23:
        h=0
    print("La hora mas un segundo es: " ,h,":",min,":",seg)
else:
    print("Ingrese una hora valida Gil: ")