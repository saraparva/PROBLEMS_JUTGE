persona=input()
while persona!="#":
    semana="Lunes""Martes""Miércoles""Jueves""Viernes"
    finde="Sábado""Domingo""Festivos"
    a,b,c=persona.split()
    dia=a
    edad=b
    peli=c
    if dia in semana:
        if edad=="Niños":
            precio=5
        if edad=="Adultos":
            precio=7.5
        if edad=="Mayores" or edad=="Estudiantes":
            precio=6.5

        
    if dia in finde:
        if edad=="Niños":
            precio=6
        if edad=="Adultos":
            precio=8.5
        if edad=="Mayores" or edad=="Estudiantes":
            precio=7.5

       
    print(str(precio)+" euros")
    persona=input()
