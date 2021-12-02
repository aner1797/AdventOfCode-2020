count = 0

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')


for item in content_list:
    Range, char, passw = item.split()
    minR, maxR = Range.split('-')
    minR = int(minR)-1
    maxR = int(maxR)-1
    char = char.replace(':', '')
    tmpCount = 0
    if passw[minR] == char:
        tmpCount +=1
    if passw[maxR] == char:
        tmpCount +=1
    if tmpCount == 1:
        count +=1

print(count)