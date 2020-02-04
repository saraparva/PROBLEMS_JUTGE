a,b,c=input().split()
d,e,f=input().split()
g,h,i=input().split()

a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
g=int(g)
h=int(h)
i=int(i)

if (((a*e*i)+(d*h*c)+(b*f*g))-((c*e*g)+(b*d*i)+(f*h*a)))==0:
    print("No es invertible.")

else:
    print("Es invertible.")
