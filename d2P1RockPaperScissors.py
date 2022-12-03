f = open("inputD2.txt","r")
lines = f.readlines()

total = 0

for line in lines: 
    #print(line[0])
    #print(line[2])
    if (line[0] == 'A' and line[2] == 'X'):
        #print("Rock, Rock, Draw")
        total = total + 1 + 3
    elif (line[0] == 'A' and line[2] == 'Y'):
        #print("Rock, Paper, Win")
        total = total + 2 + 6
    elif (line[0] == 'A' and line[2] == 'Z'):
        #print("Rock, Scissors, Lose")
        total = total + 3 + 0
    elif (line[0] == 'B' and line[2] == 'X'):
        #print("Paper, Rock, Lose")
        total = total + 1 + 0
    elif (line[0] == 'B' and line[2] == 'Y'):
        #print("Paper, Paper, Draw")
        total = total + 2 + 3
    elif (line[0] == 'B' and line[2] == 'Z'):
        #print("Paper, Scissors, Win")
        total = total + 3 + 6
    elif (line[0] == 'C' and line[2] == 'X'):
        #print("Scissors, Rock, Win")
        total = total + 1 + 6
    elif (line[0] == 'C' and line[2] == 'Y'):
        #print("Scissors, Paper, Lose")
        total = total + 2 + 0
    elif (line[0] == 'C' and line[2] == 'Z'):
        #print("Scissors, Scissors, Draw")
        total = total + 3 + 3


print(total)

f.close