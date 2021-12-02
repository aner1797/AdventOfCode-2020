val1 = 0
val2 = 0

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for x in content_list:
    val1 = x
    for y in content_list:
        val2 = int(val1) + int(y)
        for z in content_list:
            tmp = int(val2) + int(z)
            if tmp == 2020:
                print(int(val1), int(y), int(z))
                print(int(val1) * int(y) * int(z))