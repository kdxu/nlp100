def ngram(text, radix):
    return [text[i:i + radix] for i in range(len(text) - radix + 1)]


def ngram_union(text1, text2, radix):
    return set(ngram(text1, radix)) | set(ngram(text2, radix))


def ngram_intersection(text1, text2, radix):
    return set(ngram(text1, radix)) & set(ngram(text2, radix))


def ngram_difference(text1, text2, radix):
    return set(ngram(text1, radix)) - set(ngram(text2, radix))


text1 = "paraparaparadise"
text2 = "paragraph"

print(ngram_union(text1, text2, 2))
print(ngram_intersection(text1, text2, 2))
print(ngram_difference(text1, text2, 2))

print("se" in ngram_intersection(text1, text2, 2))
