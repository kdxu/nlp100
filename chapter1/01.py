def extract_odd(text):
    str_list = list(text)
    return "".join([ str_list[i] for i in range(len(str_list)) if i % 2 != 0])


print(extract_odd("パタトクカシーー"))
