

class TreeNode:
  def __init__(self, data,parent):
    self.parent = parent
    self.data = data
    self.childs = []

def printAllChilds(node,level = 0):
    print("  "*level, ":", node.data)
    for child in node.childs:
        printAllChilds(child, level+1)


dirTree = None

currentDirectory = ""

f = open("file.txt","r")

f = [x for x in f if x != "$ ls\n"]


for line in f:
    line = line.replace("$ ", "").replace("\n", "")

    if "cd" in line:
        line = line.replace("cd ","")


        if dirTree == None:
            print("Creato albero con radice ", line)
            dirTree = TreeNode(data=line, parent=None)
            currentDirectory = dirTree
        elif line != "..":
                #print("Creazione figlio di " , currentDirectory, " con nome ", line)
                nodo = currentDirectory
                nodoDaAggiungere = TreeNode(data=line,parent=currentDirectory)
                nodo.childs.append(nodoDaAggiungere)
                currentDirectory = nodoDaAggiungere
        else:
            currentDirectory = currentDirectory.parent


    
    elif "dir" not in line:
        lst = line.split(" ")

        if "ls" not in lst[0]:
            currentDirectory.childs.append(TreeNode(data=lst[0],parent=currentDirectory))

        
printAllChilds(dirTree)

#create a function that calculates the sum of all the childs of a node

totalSpace = 0
min = 2**999

totalDiskSpace = 70000000
requiredSpace = 30000000

def sumChilds(node):
    global totalSpace
    sum = 0
    for child in node.childs:
        if child.data.isdigit():
            sum += int(child.data)
        else:
            sum += sumChilds(child)
        totalSpace+=sum
    return sum


occupedSpace = sumChilds(dirTree)

def getSmallestDirBigEnough(node):
    global min
    global requiredSpace
    global occupedSpace

    thisSum = 0

    x = requiredSpace - (totalDiskSpace - occupedSpace)

    print("------------------")
    print("\nNEW FOLDER LEVEL\n ")

    if thisSum > 0:
        print("\nTotal Sum OF THE DIR: ", thisSum)

    for child in node.childs:
        if child.data.isdigit():
            print("\nChild: ", child.data)
            thisSum += int(child.data)
            print("Sum: ", thisSum)
        else:
            getSmallestDirBigEnough(child)
            
    return min





dirToDelete = getSmallestDirBigEnough(dirTree)

print("\n\nSmallest dir big enough: ", dirToDelete)

print("Occuped space: ", occupedSpace)
print("Free space: ", totalDiskSpace - occupedSpace)

