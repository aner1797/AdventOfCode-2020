import math
import collections

number = 144381670
tmpList = []

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')
finalList = []

for i in range(len(content_list)):
    finalList.append(int(content_list[i]))

finalList.sort()

print(finalList)
prev = 0
count1 = 0
count3 = 0

for num in finalList:
    diff = num - prev
    prev = num
    if diff == 1:
        count1 += 1
    if diff == 3:
        count3 += 1

print(count1, count3)



combinations = collections.defaultdict(int, {0: 1})
for adapter in finalList:
    combinations[adapter] = combinations[adapter - 1] + combinations[adapter - 2] + combinations[adapter - 3]

print(combinations[finalList[-1]])