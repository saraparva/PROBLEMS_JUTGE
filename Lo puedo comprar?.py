a=int(input())
b=int(input())

if a>b and (a-b)==1:
    print("Si te lo compras te sobrará "+str(a-b)+" euro")

if a>b and (a-b)!=1:
    print("Si te lo compras, te sobrarán "+str(a-b)+" euros")

if a==b:
    print("Si te lo compras te quedarás sin dinero")

if a<b and (b-a)==1:
    print("No te lo puedes comprar, te falta "+str(b-a)+" euro")

if a<b and (b-a)!=1:
    print("No te lo puedes comprar, te faltan "+str(b-a)+" euros")
