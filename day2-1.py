
f = open("day2-data.txt", "r")
data = f.readlines()

count3 = 0
count2 = 0
for line in data:
    has3 = False
    has2 = False
    letters = set()
    for char in line:
        if char in letters:
            continue
        if line.count(char) == 3:
            has3 = True
        elif line.count(char) == 2:
            has2 = True
    if has3:
        count3 += 1
    if has2:
        count2 += 1

print(count3 * count2)

