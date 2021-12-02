import math
import collections
from copy import deepcopy


direction = 0
location = [0, 0]
waypoint = [1, 10]

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')


for row in content_list:
    val = int(row[1:])
    sign = row[0]

    if sign == 'N':
        waypoint[0] += val
    if sign == 'S':
        waypoint[0] -= val
    if sign == 'E':
        waypoint[1] += val
    if sign == 'W':
        waypoint[1] -= val
    if sign == 'L':
        degree = (val/90) % 4
        tmp = waypoint[0]
        tmp2 = waypoint[1]
        print(degree)
        print(waypoint)

        if degree == 0:
            continue
        if degree == 1:
            if tmp > 0:
                waypoint[1] = tmp*-1
            elif tmp < 0:
                waypoint[1] = tmp*-1
            else:
                waypoint[1] = tmp

            if tmp2 > 0:
                waypoint[0] = tmp2
            elif tmp2 < 0:
                waypoint[0] = tmp2
            else:
                waypoint[0] = tmp2

        if degree == 2:
            waypoint[0] = tmp*-1
            waypoint[1] = tmp2*-1
        if degree == 3:
            if tmp > 0:
                waypoint[1] = tmp
            elif tmp < 0:
                waypoint[1] = tmp
            else:
                waypoint[1] = tmp

            if tmp2 > 0:
                waypoint[0] = tmp2*-1
            elif tmp2 < 0:
                waypoint[0] = tmp2*-1
            else:
                waypoint[0] = tmp2
        print(waypoint)

    if sign == 'R':
        degree = (val/90) % 4
        tmp = waypoint[0]
        tmp2 = waypoint[1]
        if degree == 0:
            continue
        if degree == 1:
            if tmp > 0:
                waypoint[1] = tmp
            elif tmp < 0:
                waypoint[1] = tmp
            else:
                waypoint[1] = tmp

            if tmp2 > 0:
                waypoint[0] = tmp2*-1
            elif tmp2 < 0:
                waypoint[0] = tmp2*-1
            else:
                waypoint[0] = tmp2

        if degree == 2:
            waypoint[0] = tmp*-1
            waypoint[1] = tmp2*-1
        if degree == 3:
            if tmp > 0:
                waypoint[1] = tmp*-1
            elif tmp < 0:
                waypoint[1] = tmp*-1
            else:
                waypoint[1] = tmp

            if tmp2 > 0:
                waypoint[0] = tmp2
            elif tmp2 < 0:
                waypoint[0] = tmp2
            else:
                waypoint[0] = tmp2
    if sign == 'F':
        location[0] += waypoint[0] * val
        location[1] += waypoint[1] * val

print(location)

distance = abs(location[0]) +abs(location[1])

print(distance)