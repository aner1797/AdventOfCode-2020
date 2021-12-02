import math

finalCount = 0
tmpList = ['vibrant green', 'faded magenta', 'striped cyan', 'dark plum', 'vibrant yellow', 'dark yellow', 'dark silver', 'dark tomato', 'dim chartreuse', 'dull gray', 'striped orange', 'dotted lime', 'dim black', 'dark orange', 'shiny gray', 'faded brown', 'dark lavender', 'muted plum', 'striped white', 'plaid teal', 'posh aqua', 'faded fuchsia', 'dim silver', 'bright brown', 'posh plum', 'light brown', 'posh tomato', 'light plum', 'striped aqua', 'dark white', 'dim purple', 'drab turquoise', 'dim tan', 'vibrant tan', 'muted yellow', 'muted green', 'muted brown', 'dotted fuchsia', 'vibrant gray', 'mirrored green', 'pale lavender', 'light indigo', 'dotted crimson', 'striped salmon', 'clear orange', 'shiny silver', 'clear crimson', 'mirrored brown', 'dotted purple', 'wavy orange', 'dull yellow', 'drab salmon', 'wavy tan', 'clear magenta', 'dim beige', 'faded green', 'light red', 'light gray', 'light teal', 'muted teal', 'vibrant salmon', 'mirrored gold', 'faded lime', 'plaid cyan', 'dotted maroon', 'light violet', 'clear yellow', 'mirrored white', 'dull silver', 'mirrored beige', 'dark teal', 'dark bronze', 'bright cyan', 'dull lavender', 'posh tan', 'muted silver', 'mirrored turquoise', 'clear coral', 'clear teal', 'striped tomato', 'light maroon', 'faded purple', 'drab aqua', 'striped olive', 'light black', 'dull brown', 'shiny salmon', 'wavy beige', 'clear lime', 'plaid green', 'dull tan', 'clear bronze', 'wavy lime', 'dotted chartreuse', 'vibrant coral', 'shiny yellow', 'wavy purple', 'pale aqua', 'pale black', 'dotted coral', 'plaid magenta', 'striped lavender', 'striped magenta', 'vibrant blue', 'drab olive', 'plaid bronze', 'vibrant black', 'wavy magenta', 'dotted tan', 'dark gray', 'bright white', 'faded tan', 'mirrored red', 'wavy salmon', 'faded chartreuse', 'posh crimson', 'wavy lavender', 'vibrant aqua', 'dim magenta', 'pale chartreuse', 'mirrored black', 'pale orange', 'dull tomato', 'dim coral', 'striped maroon', 'dark black', 'muted aqua', 'bright beige', 'pale yellow', 'vibrant turquoise', 'mirrored coral', 'faded indigo', 'bright lime', 'drab violet', 'dull olive', 'wavy indigo', 'posh indigo', 'plaid brown', 'striped plum', 'light fuchsia', 'drab gold', 'shiny violet', 'drab brown', 'pale purple', 'bright coral', 'striped brown', 'mirrored bronze', 'light beige', 'posh lime', 'vibrant teal', 'mirrored yellow', 'dull white', 'drab chartreuse', 'plaid fuchsia', 'drab black', 'dotted aqua', 'dim indigo', 'faded turquoise', 'dull violet', 'drab indigo', 'mirrored crimson', 'wavy fuchsia', 'striped yellow', 'dim aqua', 'wavy maroon', 'drab blue', 'shiny brown', 'mirrored violet', 'dim green', 'dull salmon', 'bright blue', 'vibrant plum', 'bright indigo', 'plaid lime', 'muted tan', 'plaid tan', 'dull beige', 'drab red', 'drab gray', 'muted red', 'drab green', 'dim gray', 'dim maroon', 'muted beige', 'bright salmon', 'muted gray', 'bright gold', 'plaid violet', 'shiny crimson', 'posh gold', 'light bronze', 'dotted cyan', 'dim salmon', 'wavy aqua', 'pale beige', 'light magenta', 'dull crimson', 'drab orange', 'striped green', 'shiny indigo', 'drab yellow', 'dark aqua', 'dim violet', 'dotted plum', 'drab maroon', 'drab coral', 'vibrant chartreuse', 'posh maroon', 'posh chartreuse', 'light blue', 'faded tomato', 'posh blue', 'dim bronze', 'dim tomato', 'vibrant white', 'dark blue', 'dotted indigo', 'posh green', 'mirrored aqua', 'dark crimson', 'wavy chartreuse', 'dull chartreuse', 'plaid crimson', 'dim lime', 'vibrant lavender', 'muted black', 'light purple', 'dark magenta', 'shiny cyan', 
'dotted tomato', 'muted cyan', 'dotted yellow', 'drab white', 'plaid aqua', 'shiny plum', 'plaid maroon', 'light cyan', 'faded silver', 'dark salmon', 'plaid orange', 'dark indigo', 'clear violet', 'dotted brown', 'shiny bronze', 'dim plum', 'drab tomato', 'dull magenta', 'plaid yellow', 'vibrant beige', 'bright yellow', 'plaid plum', 'vibrant crimson', 'vibrant orange', 'dull bronze', 'vibrant tomato', 'dark chartreuse', 'shiny red', 'wavy brown', 'mirrored chartreuse', 'pale turquoise', 'dark tan', 'faded white', 'dark gold', 'dull blue', 'drab silver', 'mirrored gray', 'mirrored teal', 'striped lime', 'wavy coral', 'dim fuchsia', 'light lime', 'dull green', 'mirrored salmon', 'faded orange', 'drab crimson', 'pale crimson', 'dark beige', 'bright teal', 'shiny maroon', 'pale plum', 'clear gold', 'mirrored purple', 'dim lavender', 'drab tan', 'vibrant lime', 'pale lime', 'drab magenta', 'posh turquoise', 'striped black', 'wavy crimson', 'pale blue', 'striped beige', 'dim gold', 'light tan', 'dark fuchsia', 'bright silver', 'posh orange', 'dark lime', 'dotted orange', 'faded cyan', 'shiny coral', 'muted fuchsia', 'bright olive', 'mirrored maroon', 'shiny black', 'wavy teal', 'dotted bronze', 'posh purple', 'shiny magenta', 'dim olive', 'striped indigo', 'wavy plum', 'pale green', 'dull fuchsia', 'dim yellow', 'dull maroon', 'dim turquoise', 'muted lime', 'bright black', 'vibrant maroon', 'pale fuchsia', 'bright magenta', 'dim crimson', 'posh red', 'shiny white', 'plaid red', 'muted coral', 'posh violet', 'dim white', 'light orange', 'shiny fuchsia', 'mirrored indigo', 'pale gray', 'bright gray', 'striped silver', 'mirrored magenta', 'faded gray', 'light green', 'clear black', 'wavy gray', 'faded black', 'bright green', 'light yellow', 'wavy tomato', 'striped coral', 'plaid lavender', 'wavy white', 'pale tan', 'wavy violet', 'dull red', 'light chartreuse', 'wavy olive', 'dull coral', 'muted orange', 'pale magenta', 'dull gold', 'clear plum', 'clear lavender', 'pale violet', 'clear olive', 'vibrant red', 'dotted olive', 'clear maroon', 'muted indigo', 'pale silver', 'plaid gray', 'muted magenta', 'pale brown', 'shiny green', 'shiny tomato']

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

count = 0
allNames = []
for item in content_list:
    tmp = item.split(',')
    name = []
    name.append(tmp[0].split(' ')[0]+" "+tmp[0].split(' ')[1])
    for bag in tmp:
        tmpBag = bag.split(' ')
        name.append(tmpBag[-4]+" "+tmpBag[-3]+" "+tmpBag[-2])
    allNames.append(name)






def recursive(color):
    if color == "contain no other":
        return 0
    
    times = color.split(' ')[0]
    color = color.split(' ')[1]+" "+color.split(' ')[2]
    total = 0

    for item in allNames:
        if item[0] == color:
            for x in item[1:]:
                total += recursive(x)

    return int(times) + (int(times) * total)



t = recursive('1 shiny gold') - 1
print(t)