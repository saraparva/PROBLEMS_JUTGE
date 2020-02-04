a,b=input().split()
num=int(a)
month=int(b)

div=num/month
decimal="0.1""0.2""0.3""0.4""0.5""0.6""0.7""0.8""0.9"

number=div-int(div)
numfin=round(number,2)

if str(numfin) in decimal:
    print("1")

else:
    print("0")
  


