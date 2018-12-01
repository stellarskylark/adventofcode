f = open("day1-1-data.txt", "r")

result = 0
for line in f.readlines():
    sign = line[0]
    val = int(line[1:])
    if sign == "+":
        result += val
    else:
        result -= val

print(result)
