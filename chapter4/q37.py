'''
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ
'''

import matplotlib.pyplot as plt
from q30 import parse_neko_text_list

'''
棒グラフ
left = [1, 2, 3]  # グラフの横軸（X軸）
height = [3, 5, 0]  # 値（Y軸）
 
plt.bar(left, height)
plt.show()


pip freeze > requirements.txt
'''

text_list = parse_neko_text_list()

result = {}
for item in text_list:
    word = item["surface"]
    if word in result:
        result[word] += 1
    else:
        result[word] = 1


sorted_result = sorted(result.items(), key=lambda x:x[1] * -1)
# 先頭 10 個
data = sorted_result[:10]

cleaned_data = list(map(list, zip(*data)))
'''
zip([1,2,3],[4,5,6],[7,8,9])
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
'''
# [('の', 9194), ('。', 7486), ('て', 6873), ('、', 6772), ('は', 6422), ('に', 6268), ('を', 6071), ('と', 5515), ('が', 5339), ('た', 3989)]
left = cleaned_data[0]  # グラフの横軸（X軸）
height = cleaned_data[1]  # 値（Y軸）
# 文字化けするよ
plt.bar(left, height)
plt.show()
# save as png
plt.savefig('figure37.png')