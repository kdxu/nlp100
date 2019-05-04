def count_line(file_name):
    return sum(1 for line in open(file_name))


print(count_line('hightemp.txt'))
