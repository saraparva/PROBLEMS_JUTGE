a,b,c=input().split()

tamaño=a
ingredientes=int(b)
extra=int(c)

if tamaño=="M" and extra==1:
    print(str(4+(ingredientes*1)+2))

if tamaño=="M" and extra==0:
    print(str(4+(ingredientes*1)))
    
if tamaño=="F" and extra==1:
    print(str(9+(ingredientes*2)+3))

if tamaño=="F" and extra==0:
    print(str(9+(ingredientes*2)))
    

