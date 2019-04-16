def join_across(text1, text2):
    list1 = list(text1)
    list2 = list(text2)
    joined = []
    for (char1, char2) in zip(list1,list2):
        joined.append(char1)
        joined.append(char2)
    return "".join(joined)


print(join_across("パトカー","タクシー"))
print(join_across("パトカーアイウエオ","タクシー"))
print(join_across("パトカー","タクシー１２３４"))