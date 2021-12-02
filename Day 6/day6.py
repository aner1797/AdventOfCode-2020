import math

finalCount = 0
tmpList = []
count = 0
endResult = []

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")


for item in content_list:
    count += 1
    for char in item:
        tmpList.append(char)
    
    if len(item) == 0:
        count -= 1
        for check in tmpList:
            if tmpList.count(check) == count:
                if check in endResult:
                    continue
                else:
                    endResult.append(check)
        finalCount += len(endResult)
        endResult = []
        tmpList = []
        count = 0

print(finalCount)