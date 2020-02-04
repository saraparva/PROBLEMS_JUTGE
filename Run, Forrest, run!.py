import sys
sum = 0

for line in sys.stdin:
    data = line.split()
    
for i in data:
    sum = sum + (int(i)*1.6)
    
if sum >= 622:
  print("Yes")
else:
    print("No")
