#get the number of the stacks
f = open("stacks.txt", "r")
stacks = [

]



for index,line in enumerate(f):
    if len(line) > 1 and line[1].isdigit():
        numberOfStacks = int(line.strip()[len(line.strip()) - 1])

        numberOfLinesWithLetters = index


f.close()




#get the stacks

f = open("stacks.txt", "r")

lines = f.readlines()[:numberOfLinesWithLetters][::-1]

for _ in range(0, numberOfStacks):
    stacks.append([])


for line in lines:

    for index, element in enumerate(line):
        if element.isupper():
            stackIndex = index // 4
            stacks[stackIndex].append(element)

print(stacks)


f.close()


#Read moves
def firstPart():
    f = open("stacks.txt", "r")

    lines = f.readlines()[numberOfLinesWithLetters+2:]

    for line in lines:
        line = line.replace("move", "")
        line = line.replace("from", "")
        line = line.replace("to", "")
        line = line.replace("\n", "")

        moves = line.split()

        numberOfPops = int(moves[0])
        fromStack = int(moves[1])-1
        toStack = int(moves[2])-1

    for _ in range(0, numberOfPops):
        stacks[toStack].append(stacks[fromStack].pop())

    finalMessage = ""

    for stack in stacks:
        finalMessage += stack.pop()
            
    print(finalMessage)

    f.close()





def secondPart():
    f = open("stacks.txt", "r")

    lines = f.readlines()[numberOfLinesWithLetters+2:]

    for line in lines:
        line = line.replace("move", "")
        line = line.replace("from", "")
        line = line.replace("to", "")
        line = line.replace("\n", "")

        moves = line.split()

        numberOfPops = int(moves[0])
        fromStack = int(moves[1])-1
        toStack = int(moves[2])-1

        datasToPush = []

        for _ in range(0, numberOfPops):
            datasToPush.append(stacks[fromStack].pop())

        datasToPush.reverse()

        stacks[toStack] += datasToPush

    datasToPush = []

    finalMessage = ""

    for stack in stacks:
        finalMessage += stack.pop()
            
    print(finalMessage)

    f.close()


secondPart()