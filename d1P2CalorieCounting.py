f = open("inputD1.txt","r")
lines = f.readlines()

#for line in lines:
    #print(line)

temp = 0 
max1 = 0
max2 = 0
max3 = 0


for line in lines: 
    if (line == "\n"):
        if (temp > max3 and temp <= max2):
            max3 = temp
        elif (temp > max2 and temp <= max1):
            max3 = max2
            max2 = temp
        elif (temp > max1):
            max3 = max2
            max2 = max1
            max1 = temp
        temp = 0
    else: 
        temp = temp + int(line)

print (max1)
print(max2)
print(max3)
print (max1 + max2 + max3)

f.close