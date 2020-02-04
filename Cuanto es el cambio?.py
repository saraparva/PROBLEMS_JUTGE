text=input()
while text!="#":
    a,b=text.split()
    precio=float(a)
    paga=float(b)
    cambio=(paga-precio)
    
    print(cambio)
    text=input()

    
