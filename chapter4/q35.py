'''
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

from q30 import parse_neko_text_list
list = parse_neko_text_list()

# print('\n'.join(map(str, list[:50])))

max_count = 0
index = 0
count = 0
for i,item in enumerate(list):
    if item['pos'] == "名詞":
        count += 1
    else:
        if count > max_count:
            index = i
            max_count = count
        count = 0

print(index)
print(max_count)

result = list[index-max_count:index]
print('\n'.join(map(str, result)))
# print('\n'.join(map(str, list[index-max_count - 10:index + 10])))