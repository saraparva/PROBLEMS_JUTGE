text=input()
numeros="0123456789"
while text!="#":
    result=0
    for i in text:
        if i in numeros:
            result+=int(i)
    print(result)
    text=input()
