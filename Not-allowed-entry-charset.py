cadena=input()
nonum=input()
output=""
for i in cadena:
    if not (i in nonum):
        output+=i
print(output)
