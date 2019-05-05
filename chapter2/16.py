import sys

file = "hightemp.txt"
output = "divided"

i = 0
char = 96

with open(file) as f:
    for row in f:
        if i % int(sys.argv[1]) == 0:
            char += 1
            with open(output + chr(char), "w") as w:
                w.write(row)
        else:
            with open(output + chr(char), "a") as w:
                w.write(row)
        i += 1