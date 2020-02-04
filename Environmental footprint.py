text=input()

while text!="#":
    transport, energyprop=text.split()
    energyprop=int(energyprop)
    
    if transport=="Ship":
        energy=0.3
        km=energyprop/energy
        carbon=km*23.3
        
    if transport=="Train":
        energy=0.32
        km=energyprop/energy
        carbon=km*23.1
        
    if transport=="Road":
        energy=2.12
        km=energyprop/energy
        carbon=km*160.1
        
    if transport=="Plane":
        energy=21.01
        km=energyprop/energy
        carbon=km*1577.1

    text=input()
    print(transport+" "+str(round(km, 1))+" "+str(round(carbon, 1)))

