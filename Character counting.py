text=input()

uppers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers="abcdefghijklmnopqrstuvwxyz"
outup=""
outlow=""
outoth=""

for i in text:
    if i!=" ":
        if i in uppers:
            outup+=i
        elif i in lowers:
            outlow+=i
        else:
            outoth+=i
            
print("Uppercase "+str(len(outup)))
print("Lowercase "+str(len(outlow)))
print("Other "+str(len(outoth)))


