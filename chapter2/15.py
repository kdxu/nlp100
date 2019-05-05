import sys


def count_line(file_name):
    return sum(1 for line in open(file_name))


file = "hightemp.txt"
count = count_line(file)
with open(file) as f:
    for i, row in enumerate(f):
        if count - i > int(sys.argv[1]):
            continue
        print(row, end="")
