import sys
f = open("day1-1-data.txt", "r")

freqs = set()
freqs.add(0)
freq = 0
changes = [int(x) for x in f.readlines()]

while True:
    for val in changes:
        freq += val
        if freq in freqs:
            print("The answer is: ", freq)
            sys.exit(0)
        else:
            freqs.add(freq)

