
f = open("inputD3.txt","r")
lines = f.readlines()

fulllist = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total = 0

for line in lines:
    fulllist.append(line)
  
for x in fulllist:
    firsthalf = []
    secondhalf = []
    length =  len(x)
    #print("Full " + str(length))
    half = len(x) // 2
    #print("Half " + str(half))
    firsthalf.append(x[0:half])
    secondhalf.append(x[half:length-1])
    for y in firsthalf[0]:
        if y in secondhalf[0]:
            total = total + alphabet.index(y) +1
            break

print("Total is " + str(total))