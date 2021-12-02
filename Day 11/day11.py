import math
import collections
from copy import deepcopy


number = 144381670
tmpList = []

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')
finalList = []
for row in content_list:
    finalList.append(list(row))

newList = deepcopy(finalList)

while True:
    changes = 0
    finalList = deepcopy(newList)

    for i in range(len(finalList)):
        for j in range(len(finalList[i])):
            count = 0
            tmpI = i
            tmpJ = j
            while True:
                if tmpI-1 in range(len(finalList)) and tmpJ-1 in range(len(finalList[tmpI-1])) and finalList[tmpI-1][tmpJ-1] == '#':
                    count += 1
                    break
                if tmpI-1 in range(len(finalList)) and tmpJ-1 in range(len(finalList[tmpI-1])) and finalList[tmpI-1][tmpJ-1] == 'L':
                    break
                if tmpI-1 not in range(len(finalList)) or tmpJ-1 not in range(len(finalList[tmpI-1])):
                    break
                tmpI -= 1
                tmpJ -= 1
            tmpI = i
            tmpJ = j
            while True:
                if tmpI-1 in range(len(finalList)) and tmpJ in range(len(finalList[tmpI-1])) and finalList[tmpI-1][tmpJ] == '#':
                    count += 1
                    break
                if tmpI-1 in range(len(finalList)) and tmpJ in range(len(finalList[tmpI-1])) and finalList[tmpI-1][tmpJ] == 'L':
                    break
                if tmpI-1 not in range(len(finalList)) or tmpJ not in range(len(finalList[tmpI-1])):
                    break
                tmpI -= 1
            tmpI = i
            tmpJ = j
            while True:
                if tmpI-1 in range(len(finalList)) and tmpJ+1 in range(len(finalList[tmpI-1])) and finalList[tmpI-1][tmpJ+1] == '#':
                    count += 1
                    break
                if tmpI-1 in range(len(finalList)) and tmpJ+1 in range(len(finalList[tmpI-1])) and finalList[tmpI-1][tmpJ+1] == 'L':
                    break
                if tmpI-1 not in range(len(finalList)) or tmpJ+1 not in range(len(finalList[tmpI-1])):
                    break
                tmpI -= 1
                tmpJ += 1
            tmpI = i
            tmpJ = j
            while True:
                if tmpI in range(len(finalList)) and tmpJ-1 in range(len(finalList[tmpI])) and finalList[tmpI][tmpJ-1] == '#':
                    count += 1
                    break
                if tmpI in range(len(finalList)) and tmpJ-1 in range(len(finalList[tmpI])) and finalList[tmpI][tmpJ-1] == 'L':
                    break
                if tmpI not in range(len(finalList)) or tmpJ-1 not in range(len(finalList[tmpI])):
                    break
                tmpJ -= 1
            tmpI = i
            tmpJ = j
            while True:
                if tmpI in range(len(finalList)) and tmpJ+1 in range(len(finalList[tmpI])) and finalList[tmpI][tmpJ+1] == '#':
                    count += 1
                    break
                if tmpI in range(len(finalList)) and tmpJ+1 in range(len(finalList[tmpI])) and finalList[tmpI][tmpJ+1] == 'L':
                    break
                if tmpI not in range(len(finalList)) or tmpJ+1 not in range(len(finalList[tmpI])):
                    break
                tmpJ += 1
            tmpI = i
            tmpJ = j
            while True:
                if tmpI+1 in range(len(finalList)) and tmpJ-1 in range(len(finalList[tmpI+1])) and finalList[tmpI+1][tmpJ-1] == '#':
                    count += 1
                    break
                if tmpI+1 in range(len(finalList)) and tmpJ-1 in range(len(finalList[tmpI+1])) and finalList[tmpI+1][tmpJ-1] == 'L':
                    break
                if tmpI+1 not in range(len(finalList)) or tmpJ-1 not in range(len(finalList[tmpI+1])):
                    break
                tmpI += 1
                tmpJ -= 1
            tmpI = i
            tmpJ = j
            while True:
                if tmpI+1 in range(len(finalList)) and tmpJ in range(len(finalList[tmpI+1])) and finalList[tmpI+1][tmpJ] == '#':
                    count += 1
                    break
                if tmpI+1 in range(len(finalList)) and tmpJ in range(len(finalList[tmpI+1])) and finalList[tmpI+1][tmpJ] == 'L':
                    break
                if tmpI+1 not in range(len(finalList)) or tmpJ not in range(len(finalList[tmpI+1])):
                    break
                tmpI += 1
            tmpI = i
            tmpJ = j
            while True:
                if tmpI+1 in range(len(finalList)) and tmpJ+1 in range(len(finalList[tmpI+1])) and finalList[tmpI+1][tmpJ+1] == '#':
                    count += 1
                    break
                if tmpI+1 in range(len(finalList)) and tmpJ+1 in range(len(finalList[tmpI+1])) and finalList[tmpI+1][tmpJ+1] == 'L':
                    break
                if tmpI+1 not in range(len(finalList)) or tmpJ+1 not in range(len(finalList[tmpI+1])):
                    break
                tmpI += 1
                tmpJ += 1

            
            if finalList[i][j] == 'L' and count == 0:
                newList[i][j] = '#'
                changes +=1
            if finalList[i][j] == '#' and count >= 5:
                newList[i][j] = 'L'
                changes +=1

    if changes == 0:
        break

occupied = 0
for i in range(len(newList)):
        for j in range(len(newList[i])):
            if newList[i][j] == '#':
                occupied += 1

print(occupied)