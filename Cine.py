persona=input()
while persona!="#":
    semana="Lunes""Martes""Miércoles""Jueves""Viernes"
    finde="Sábado""Domingo""Festivos"
    a,b,c=persona.split()
    dia=a
    edad=b
    peli=c
    if peli=="2D":
        if dia in semana:
            if edad=="Niños":
                precio=5
            if edad=="Adultos":
                precio=7.5
            else:
                precio=6.5
        if dia in finde:
            if edad=="Niños":
                precio=6
            if edad=="Adultos":
                precio=8.5
            else:
                precio=7.5
    if peli=="3D":
        if dia in semana:
            if edad=="Niños":
                precio=6
            if edad=="Adultos":
                precio=8.5
            else:
                precio=7.5
        if dia in finde:
            if edad=="Niños":
                precio=7
            if edad=="Adultos":
                precio=9.5
            else:
                precio=8.5
        
    print(str(precio)+" euros")
    persona=input()
    
