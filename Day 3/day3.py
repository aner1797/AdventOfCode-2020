move = 0
tree = 0

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

for i in range(2, len(content_list), 2):
    move = (move + 1) % len(content_list[i])
    if content_list[i][move] == "#":
        tree += 1



print(tree)