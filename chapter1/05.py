def ngram(text, radix):
    return [text[i:i + radix] for i in range(len(text) - radix + 1)]


print(ngram("I am an NLPer".split(), 2))
print(ngram("I am an NLPer", 2))
