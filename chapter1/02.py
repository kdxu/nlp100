def join_across(text1, text2):
    list1 = list(text1)
    list2 = list(text2)
    joined = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            joined.append(list1[i])
        if i < len(list2):
            joined.append(list2[i])
    return "".join(joined)


print(join_across("パトカー","タクシー"))
print(join_across("パトカーアイウエオ","タクシー"))
print(join_across("パトカー","タクシー１２３４"))