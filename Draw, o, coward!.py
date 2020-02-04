frase=input()
letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
while frase!="Palindrome!":
    cadena=""
    for i in frase:
        if i in letras:
            cadena+=i
    cadenaoriginal=cadena.lower()
    cadenaalreves=cadena[::-1]
    cadenafinal=cadenaalreves.lower()
    
    if cadenaoriginal==cadenafinal:
        print('"'+frase+'"'+" is a palindrome")

    if cadenaoriginal!=cadenafinal:
        print('"'+frase+'"'+" is not a palindrome")

    frase=input()
