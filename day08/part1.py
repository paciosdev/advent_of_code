f = open("file.txt", "r")

lines = f.readlines()

sum = 0
interni = 0

for i,line in enumerate(lines):

    line = line.replace("\n","")

    if i == 0:
        sum += len(line)
    elif i == len(lines)-1:
        sum += len(line)
    else:
        sum += 2
        #qui sei nelle righe centrali
        for index, j in enumerate(line):
            if index != 0 and index != len(line)-1:
                print("Allora, il ", j, " ha: \n")

                elementiASinistra = line[:index] 
                elementiADestra = line[index+1:]
                elementiSopra = []
                elementiSotto = []

                for k in range(i-1, -1, -1):
                    if lines[k][index] != " ":
                        elementiSopra.append(lines[k][index])
                    else:
                        break

                for k in range(i+1, len(lines)):
                    if lines[k][index] != " ":
                        elementiSotto.append(lines[k][index])
                    else:
                        break

                print("Sopra: ", elementiSopra, "\nSotto: ", elementiSotto)
                print("Sinistra: ", elementiASinistra, "\nDestra: ", elementiADestra, "\n\n")

                visibile = True

                for k in elementiSopra:
                    if int(k) >= int(j):
                        visibile = False                 
                        break
                if visibile == False:
                    visibile = True
                    for k in elementiSotto:
                        if int(k) >= int(j):
                            visibile = False
                            break
                if visibile == False:
                    visibile = True
                    for k in elementiASinistra:
                        if int(k) >= int(j):

                            visibile = False
                            break
                if visibile == False:
                    visibile = True
                    for k in elementiADestra:
                        if int(k) >= int(j):
                            visibile = False
                            break
                
                if visibile:
                    print(j, "è visibile")
                    interni += 1


                print("--------------")


print(interni + sum)

