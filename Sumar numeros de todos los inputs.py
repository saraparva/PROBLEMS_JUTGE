text=input()
numeros="0123456789"
result=0
while text!="#":
    for i in text:
        if i in numeros:
            result+=int(i)
    text=input()
print(result)
