f = open("inputD2.txt","r")
lines = f.readlines()

total = 0

for line in lines: 
    #print(line[0])
    #print(line[2])
    if (line[0] == 'A' and line[2] == 'X'):
        #print("Rock, Lose, Scissors")
        total = total + 0 + 3
    elif (line[0] == 'A' and line[2] == 'Y'):
        #print("Rock, Draw, Rock")
        total = total + 3 + 1
    elif (line[0] == 'A' and line[2] == 'Z'):
        #print("Rock, Win, Paper")
        total = total + 6 + 2
    elif (line[0] == 'B' and line[2] == 'X'):
        #print("Paper, Lose, Rock")
        total = total + 0 + 1
    elif (line[0] == 'B' and line[2] == 'Y'):
        #print("Paper, Draw, Paper")
        total = total + 3 + 2
    elif (line[0] == 'B' and line[2] == 'Z'):
        #print("Paper, Win, Scissors")
        total = total + 6 + 3
    elif (line[0] == 'C' and line[2] == 'X'):
        #print("Scissors, Lose, Paper")
        total = total + 0 + 2
    elif (line[0] == 'C' and line[2] == 'Y'):
        #print("Scissors, Draw, Scissors")
        total = total + 3 + 3
    elif (line[0] == 'C' and line[2] == 'Z'):
        #print("Scissors, Win, Rock")
        total = total + 6 + 1


print(total)

f.close