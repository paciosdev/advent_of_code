f = open("file.txt", "r")

def firstPart():
    def range_subset(range1, range2):
        if not range1:
            return True  # empty range is subset of anything
        if not range2:
            return False  # non-empty range can't be subset of empty range
        if len(range1) > 1 and range1.step % range2.step:
            return False  # must have a single value or integer multiple step
        return range1.start in range2 and range1[-1] in range2

    sum = 0

    for line in f:
        left,right = line.replace("\n", "").split(",")

        firstLeftNumber, firstRightNumber = left.split("-")

        secondLeftNumber, secondRightNumber = right.split("-")
 
    if range_subset(range(int(firstLeftNumber), int(firstRightNumber)+1), range(int(secondLeftNumber), int(secondRightNumber)+1)) or range_subset(range(int(secondLeftNumber), int(secondRightNumber)+1), range(int(firstLeftNumber), int(firstRightNumber)+1)):
        sum += 1

    print(sum)



def secondPart():

    def range_overlap(range1, range2):
        lst3 = [value for value in list(range1) if value in list(range2)]
        print(lst3)
        if len(lst3) > 0:
            return True

    total = 0

    for line in f:
        left,right = line.replace("\n", "").split(",")

        firstLeftNumber, firstRightNumber = left.split("-")

        secondLeftNumber, secondRightNumber = right.split("-")

        if range_overlap(range(int(firstLeftNumber), int(firstRightNumber)+1), range(int(secondLeftNumber), int(secondRightNumber)+1)):
            total += 1

    print(total)

secondPart()