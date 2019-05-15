import sys

file = "hightemp.txt"
output = "divided"

row1 = []

with open(file) as f:
    for row in f:
        for i, word in enumerate(row.split("\t")):
            if i == 0:
                row1.append(word)


print(list(set(row1)))