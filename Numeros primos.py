n=int(input())

if n>0:
    for i in range(1,n):
         creciente = 2
         esPrimo = True

         while esPrimo and creciente<i:
             if i%creciente==0:
                 esPrimo = False
                 
             else:
                 creciente+=1
                 
         if esPrimo:
             print(i)
            
                 
