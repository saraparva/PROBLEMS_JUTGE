text=input()
nums="1234567890"
outstr=""
outint=""

for i in text:
    if i in nums:
        outint+=i
    else:
        outstr+=i

print(outstr)
print(outint)
