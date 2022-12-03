
f = open("inputD3.txt","r")
lines = f.readlines()

fulllist = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total = 0
temp = []

for line in lines:
    fulllist.append(line)

for x in fulllist:
    if (((int(fulllist.index(x)+1) % 3)) == 0):
        temp.append(x[0:len(x)-1])
        for y in temp[0]:
            if y in temp[1] and y in temp[2]:
                total = total + alphabet.index(y) +1
                temp = []
                break


        #print("Divisible by 3 " + str(fulllist.index(x)))
    else:
        temp.append(x[0:len(x)-1])
        #print("Not divisible by 3 "+ str(fulllist.index(x)))
        #print(temp)
    
    


print("Total is " + str(total))