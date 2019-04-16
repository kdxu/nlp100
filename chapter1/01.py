def extract_odd(text):
    str_list = list(text)
    odds = []
    for i in range(len(str_list)):
        if i % 2 == 0:
            continue
        odds.append(str_list[i])
    return "".join(odds)


print(extract_odd("パタトクカシーー"))
