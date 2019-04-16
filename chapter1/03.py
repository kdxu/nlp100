def sentence_to_word_length(sentence):
    split = sentence.replace(",","").replace(".","").split(" ")
    return "".join([str(len(text)) for text in split])


print(sentence_to_word_length("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
