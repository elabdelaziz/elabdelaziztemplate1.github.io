arr = [-4, 3, -9, 0, 4, 1]

posCount = 0
negCount = 0
zeroCount = 0
arrLen = len(arr)
for i in arr:
    if (i > 0):
        posCount += 1
    elif (i < 0):
        negCount += 1
    zeroCount += 1

print("%f"%(posCount / arrLen))
print("%f"%(negCount / arrLen))
print("%f"%(zeroCount / arrLen))
 