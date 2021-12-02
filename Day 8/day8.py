import math

accCount = 0
tmpList = []

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for item in content_list:
    term, value = item.split(' ')
    value = int(value)
    tmpList.append((term, value))
    """ print(test)
    if value == "+583":
        print("found") """

index = 0
OutIndex = 0
first = True
indexList = []
print(tmpList[628])
oldList = tmpList[:]

while True:
    index = 0
    accCount = 0
    indexList = []
    if tmpList[OutIndex][0] == "jmp":
        tmpList = oldList[:]
        tmpList[OutIndex] = ("nop", tmpList[OutIndex][1])
        OutIndex += 1
    elif tmpList[OutIndex][0] == "nop":
        tmpList = oldList[:]
        tmpList[OutIndex] = ("jmp", tmpList[OutIndex][1])
        OutIndex += 1
    else:
        OutIndex += 1
        
    while True:
        move = tmpList[index]
        indexList.append(index)
        

        if move[0] == "acc":
            accCount += move[1]
            index += 1
        if move[0] == "jmp":
            index += move[1]
        if move[0] == "nop":
            index += 1

        if index == 629:
            print("Out of file")
            break
        if index in indexList:
            print("Loop")
            break
    print(accCount)
    if index == 629:
        break