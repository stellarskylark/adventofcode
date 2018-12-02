f = open("day2-data.txt", "r")
data = f.readlines()

def distance(a, b):
    dist = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dist += 1
    return dist

for line1 in data:
    for line2 in data:
        if distance(line1, line2) == 1:
            print(line1)
            print(line2)
