import math

a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)

if a==0:
    print("x="+str(c/b))

else:
    draiz=float((b*b)-4*a*c)
    
    if float(draiz)<0:
        raiz=math.sqrt((-1)*float(draiz))
        
        print("x="+str((-b)/(2*a))+"+"+str((float(raiz))/(2*a))+"i")
        print("x="+str((-b)/(2*a))+"-"+str((float(raiz))/(2*a))+"i")
        
    else:
        raiz=math.sqrt(draiz)
        sol1=(-b+float(raiz))/(2*a)
        sol2=(-b-float(raiz))/(2*a)
        
        if (float(sol1))==(float(sol2)):
            print("x="+str(float(sol1)))
            
        if float(sol1)!=float(sol2):
            print("x="+str(float(sol1)))
            print("x="+str(float(sol2)))
        





