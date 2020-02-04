cadena=input()
while cadena!=".":
    output=""
    for i in cadena:
        if i=="G":
            output+="C"
        if i=="C":
            output+="G"
        if i=="T":
            output+="A"
        if i=="A":
            output+="T"
            
    cadenainvertida=output[::-1]
    print(cadenainvertida)
    cadena=input()
