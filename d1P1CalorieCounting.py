
f = open("inputD1.txt","r")
lines = f.readlines()

#for line in lines:
    #print(line)

temp = 0 
max = 0

'''for line in lines: 
    if line is int :
        temp = temp  + line
        if temp > max : 
            max = temp
    else :
        temp = 0'''

for line in lines: 
    if (line == "\n"):
        temp = 0
    else: 
        temp = temp + int(line)
        if temp > max: 
            max = temp

print (max)

f.close