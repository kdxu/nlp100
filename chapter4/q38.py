'''
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
'''

import matplotlib.pyplot as plt
from q30 import parse_neko_text_list

''' 
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html

plt.hist(x) 
// x : (n,) array or sequence of (n,) arrays
// Input values, this takes either a single array or a sequence of arrays which are not required to be of the same length.
plt.show()
'''

text_list = parse_neko_text_list()

result = {}
for item in text_list:
    word = item["surface"]
    if word in result:
        result[word] += 1
    else:
        result[word] = 1


# sorted_result = sorted(result.items(), key=lambda x:x[1] * -1)
# 先頭 10 個
# data = sorted_result[:10]
cleaned_data = list(map(list, zip(*result.items())))
#print(cleaned_data[1][:100])

plt.hist(cleaned_data[1], bins=50, range=(1,200))
plt.show()