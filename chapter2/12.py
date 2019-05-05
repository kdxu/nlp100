def extract(file_name):
    with open(file_name) as rf:
        for i,row, in enumerate(rf):
            if i == 0:
                with open("col1.txt", mode="w") as wf:
                    wf.write(row)
            elif i == 1:
                with open("col2.txt", mode="w") as wf:
                    wf.write(row)


extract("hightemp.txt")