def cipher(text):
    return "".join([chr(219 - ord(c)) if 97 <= ord(c) <= 122 else c for c in text])


encode = cipher("Neither a borrower nor a lender be; For loan oft loses both itself and friend, And borrowing dulls the edge of husbandry.")
print(encode)
print(cipher(encode))
