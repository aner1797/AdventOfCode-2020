import math
import collections
from copy import deepcopy
from itertools import count
from sympy.ntheory.modular import crt

departure = 0
busDict = {}

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
content_list.remove('')

departure = int(content_list[0])
busses = content_list[1].split(',')

def find_bus_cadence(a, b, start, offset):
    n = start
    while (n-offset) % a != 0:
        n += b
    m = n+b
    while (m-offset) % a != 0:
        m += b
    return n, m-n


offset = 0
cadence = int(busses[0])
answer = int(busses[0])
for b in busses[1:]:
    offset += 1
    if b == 'x':
        continue
    answer, cadence = find_bus_cadence(int(b), cadence, answer, offset)
answer -= offset
print(f'The answer to part two is {answer}')







with open('input.txt') as f:
    ls = [line.strip() for line in f.readlines()]

earliest = int(ls[0])
bus_times = [(int(x), -i) for i, x in enumerate(ls[1].split(',')) if x != 'x']
busses, times = zip(*bus_times)


# Part one
print(next((time - earliest)*bus
           for time in count(earliest) for bus in busses
           if time % bus == 0))


# Part two
print(crt(busses, times)[0])