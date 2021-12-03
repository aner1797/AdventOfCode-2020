import math

number = 144381670
tmpList = []

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for i in range(25,len(content_list)):
    total = int(content_list[i])
    start = i-25
    maxIndex = i
    result = 0

    for x in range(start, maxIndex):
        first = content_list[x]
        if x != maxIndex-1:
            for y in range(x+1, maxIndex):
                second = content_list[y]
                tmpTotal = int(first) + int(second)
                if tmpTotal == total:
                    result = 1
                    break
        if result == 1:
            break
    if result == 0:
        print(total)
        break



for i in range(len(content_list)):
    tmpList = []
    tmpList.append(int(content_list[i]))
    first = int(content_list[i])
    start = i+1
    
    for x in range(start, len(content_list)):
        tmpList.append(int(content_list[x]))
        first += int(content_list[x])
        if first == number:
            print(max(tmpList) + min(tmpList))
        if first > number:
            break
        