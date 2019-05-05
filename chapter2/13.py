with open('col1.txt') as col1, open('col2.txt') as col2:
    for word1, word2 in zip(col1, col2):
        with open("merge.txt", mode="a") as merge:
            merge.write(word1.rstrip() + "\t" + word2)
