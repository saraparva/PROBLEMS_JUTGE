persona=input()
while persona!="-1":
    a,b=persona.split()
    volumen=float(a)
    bebida=b
    if bebida=="Y":
        precio=volumen*1.8
    if bebida=="N":
        precio=volumen*2
    print("{0:.2f}".format(precio))
    persona=input()
