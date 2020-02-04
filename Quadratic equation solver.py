import math
[a,b,c] = [float(x) for x in input().split()] # Calculate the square root argument
d = b*b-4*a*c

# Complex roots?

if d < 0:
    print("It has complex Roots!")
else:
# Else, print the output
    e = math.sqrt(d)
    x1=(-b+e)/(2*a)
    x2=(-b-e)/(2*a)
    print("x_+ = %.2f; x_- = %.2f" % (x1,x2))
