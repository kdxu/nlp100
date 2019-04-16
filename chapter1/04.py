def to_symbols_for_element(text):
    one_chars = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    split = text.split(" ")
    return {index+1:value[0] if index+1 in one_chars else value[0:2] for (index, value) in enumerate(split)}


symbols = to_symbols_for_element("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
print(symbols)
print(symbols[1])
print(symbols[5])
