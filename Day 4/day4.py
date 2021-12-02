import re

# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
finalCount = 0
valid ={
    "byr": 0,
    "iyr": 0,
    "eyr": 0,
    "hgt": 0,
    "hcl": 0,
    "ecl": 0,
    "pid": 0
}

# Strips the newline character 
for line in Lines:
    parsed = line.split()
    for string in parsed:
        for key in valid:
            if key in string and valid[key] == 0:
                val = string.split(':')
                if key == "byr":
                    if len(val[1]) == 4 and int(val[1]) >= 1920 and int(val[1]) <= 2002:
                        count += 1
                        valid[key] = 1
                if key == "iyr":
                    if len(val[1]) == 4 and int(val[1]) >= 2010 and int(val[1]) <= 2020:
                        count += 1
                        valid[key] = 1
                if key == "eyr":
                    if len(val[1]) == 4 and int(val[1]) >= 2020 and int(val[1]) <= 2030:
                        count += 1
                        valid[key] = 1
                if key == "hgt":
                    if val[1][-2:] == "cm" and int(val[1][:-2]) >= 150 and int(val[1][:-2]) <= 193:
                        count += 1
                        valid[key] = 1
                    if val[1][-2:] == "in" and int(val[1][:-2]) >= 59 and int(val[1][:-2]) <= 76:
                        count += 1
                        valid[key] = 1
                if key == "hcl":
                    if val[1][0] == "#" and len(val[1][1:]) == 6:
                        if re.search('[^a-f0-9]',val[1][1:],re.I):
                            continue
                        else:
                            count += 1
                            valid[key] = 1
                if key == "ecl":
                    if val[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        count += 1
                        valid[key] = 1
                if key == "pid":
                    if len(val[1]) == 9:
                        if re.search('[^0-9]',val[1],re.I):
                            continue
                        else:
                            count += 1
                            valid[key] = 1
    if line == "\n" and count == 7:
        finalCount += 1
    if line == "\n":
        count = 0
        for key in valid:
            valid[key] = 0

if count == 7:
    finalCount += 1
print(finalCount)