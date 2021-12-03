import math

minimum = 0
maximum = 127
minCol = 0
maxCol = 7
highest = 0
idList = []

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for item in content_list:
    minimum = 0
    maximum = 127
    minCol = 0
    maxCol = 7
    for char in item:
        if char == 'F':
            diff = math.floor((maximum - minimum)/2)
            maximum = minimum + diff
        if char == 'B':
            diff = math.floor((maximum - minimum)/2)
            minimum = minimum + diff + 1
        if char == 'L':
            diff = math.floor((maxCol - minCol)/2)
            maxCol = minCol + diff
        if char == 'R':
            diff = math.floor((maxCol - minCol)/2)
            minCol = minCol + diff + 1
    id = (minimum * 8) + minCol
    idList.append(id)
    if id > highest:
        highest = id

print(highest)

idList.sort()
before = idList[0]
for i in range(1, len(idList)):
    real = idList[i] - 1
    if real != before:
        print(real)
    before = idList[i]