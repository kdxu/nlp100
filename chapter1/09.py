import random


def typoglycemia(sentence):
    results = []
    for word in  sentence.split(" "):
        if len(word) <= 4:
            results.append(word)
        else:
            inner = list(word[1:-1])
            random.shuffle(inner)
            results.append(word[0] + ''.join(inner)+ word[-1])
    return results


print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))