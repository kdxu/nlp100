'''
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''

from q30 import parse_neko_text_list
text_list = parse_neko_text_list()

result = {}
for item in text_list:
    word = item["surface"]
    if word in result:
        result[word] += 1
    else:
        result[word] = 1


sorted_result = sorted(result.items(), key=lambda x:x[1] * -1)

print("\n".join(["{0}:{1}".format(key, value) for (key, value) in sorted_result[:20]]))
