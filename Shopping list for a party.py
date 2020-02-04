a=int(input())
res=a%5
if res==0:
    n=int(a/5)
else:
    num=a+(5-res)
    n=int(num/5)

print("- "+str(n*1)+" natural yogurt.")
print("- "+str(n*3)+" eggs.")
print("- "+str(n*250)+"gr flour.")
print("- "+str(n*125)+"gr cocoa powder.")
print("- "+str(n*250)+"gr sugar.")
print("- "+str(n*125)+"gr olive oil.")
print("- "+str(n*1)+" packet of yeast.")
