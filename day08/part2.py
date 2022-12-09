f = open("file.txt", "r")

lines = f.readlines()

sum = 0
interni = 0

distanze = []

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

                distanceSopra = 0
                distanceSotto = 0
                distanceSinistra = 0
                distanceDestra = 0

                for k in elementiSopra:
                    if int(k) >= int(j):
                        distanceSopra+=1
                        break
                    distanceSopra+=1

                print("sopra ", distanceSopra)

                for k in elementiSotto:
                    if int(k) >= int(j):
                        distanceSotto+=1
                        break
                    distanceSotto+=1
              
                print("sotto ", distanceSotto)

                for k in reversed(elementiASinistra):
                    if int(k) >= int(j):
                        distanceSinistra+=1
                        break
                    distanceSinistra+=1

                print("sinistra ", distanceSinistra)
               
                for k in elementiADestra:
                    if int(k) >= int(j):  
                        distanceDestra+=1    
                        break
                    distanceDestra+=1
                    
                print("destra ", distanceDestra)
                
                distanze.append(distanceSopra*distanceSotto*distanceSinistra*distanceDestra)

                print("--------------")



print(max(distanze))