import sys

with open("hightemp.txt") as f:
    for i, row in enumerate(f):
        if i >= int(sys.argv[1]):
            continue
        print(row, end="")
