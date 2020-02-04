cadena=input()
nonum=input()
while cadena!="#":
    output=""
    for i in cadena:
        if not (i in nonum):
            output+=i
    print(output)
    cadena=input()
    nonum=input()
