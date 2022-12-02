
#reading from file
f = open("file.txt", "r")

class Game:
    def __init__(self, opponentMove, myMove):
        self.opponentMove = opponentMove
        self.myMove = myMove
        
#create a list of games
games = []

for x in f:
    game = Game(x[0],x[2])
    games.append(game)

sum = 0


def calculateScore(opponentMove, myMove):

    score = 0

    if myMove == "X": 
        score += 1
    elif myMove == "Y":
        score += 2
    elif myMove == "Z":
        score += 3

    #Avversario ha scelto sasso
    if opponentMove == "A":
        if myMove == "X": 
            score += 3
        elif myMove == "Y":
            score += 6

    #Avversario ha scelto carta
    elif opponentMove == "B":
        if myMove == "Y":
            score += 3
        elif myMove == "Z":
            score += 6

    #Avversario ha scelto forbice
    elif opponentMove == "C":
        if myMove == "X":
            score += 6
        elif myMove == "Z":
            score += 3

    return score

    


for game in games:
    sum += calculateScore(game.opponentMove, game.myMove)

print(sum)


sum = 0

def calculateScore2(opponentMove, myMove):

    score = 0

    #Avversario ha scelto sasso
    if opponentMove == "A":
        if myMove == "X":
            #perdo con forbice 
            score += 3
        elif myMove == "Y":
            #pareggio con sasso 
            score += 4
        elif myMove == "Z":
            #vinco con carta 
            score += 8

    #Avversario ha scelto carta
    elif opponentMove == "B":
        if myMove == "X": 
            #perdo con sasso 
            score += 1
        elif myMove == "Y":
            #pareggio con carta 
            score += 5
        elif myMove == "Z":
            #vinco con forbice
            score += 9

    #Avversario ha scelto forbice
    elif opponentMove == "C":
        #perdo con carta 
        if myMove == "X":
            score += 2
        #pareggio con forbice
        elif myMove == "Y":
            score += 6
        #vinco con sasso
        elif myMove == "Z":
            score += 7

    return score


for game in games:
    sum += calculateScore2(game.opponentMove, game.myMove)

print(sum)