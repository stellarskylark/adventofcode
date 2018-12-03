f = open("day3-data.txt", "r")
lines = f.readlines()
coords = []
sizes = []
for l in lines:
    tail = l.split('@')[1].strip()
    c, s = tail.split(':')
    coords.append([int(x) for x in c.split(',')])
    sizes.append([int(x) for x in s.strip().split('x')])

fabric = [[0 for y in range(1000)] for x in range(1000)]

def update(x, y, w, h):
    for i in range(w):
        for j in range(h):
            fabric[x+i][y+j] += 1

for i in range(len(coords)):
    x, y = coords[i]
    w, h = sizes[i]
    update(x, y, w, h)

result = 0
for x in range(1000):
    for y in range(1000):
        if fabric[x][y] >= 2:
            result += 1

print("Part 1:", result)

def check(x, y, w, h):
    for i in range(w):
        for j in range(h):
            if fabric[x+i][y+j] > 1:
                return False
    return True

for i in range(len(coords)):
    x, y = coords[i]
    w, h = sizes[i]
    if check(x, y, w, h):
        print("Part 2:", i + 1)
        break
