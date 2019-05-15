import sys

file = "hightemp.txt"

row3 = []

with open(file) as f:
    for row in f:
        for i, word in enumerate(row.split("\t")):
            if i == 2:
                row3.append(word)

print(sorted(row3))