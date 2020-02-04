cadena=input()
output=""
while cadena!="#":
    for i in cadena:
        if i=="A":
            output+="C"
        if i=="B":
            output+="D"
        if i=="C":
            output+="A"
        if i=="D":
            output+="B"
            
    cadenainvertida=output[::-1]
    print(cadenainvertida)
    cadena=input()
    
