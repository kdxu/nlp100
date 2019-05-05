def extract(file_name):
    with open(file_name) as rf:
        for row in rf:
            for i, word in enumerate(row.split("\t")):
                if i == 0:
                    with open("col1.txt", mode="a") as wf:
                        wf.write(word + "\n")
                elif i == 1:
                    with open("col2.txt", mode="a") as wf:
                        wf.write(word + "\n")


extract("hightemp.txt")