n=int(input())
m=int(input())

suma=0
resta=0

for i in range(m):
    suma+=n+i+1

for i in range(m):
    resta+=n-i-1


print(str(suma)+" "+str(resta))
