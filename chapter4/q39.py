'''
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

https://qiita.com/sci_Haru/items/68bd9a05d99598d445b0
plt.yscale('log')
// plt.yscale(matplotlib.scale.LogScale(())
plt.xscale('log')
'''

import matplotlib.pyplot as plt
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
cleaned_data = list(map(list, zip(*sorted_result)))
left = cleaned_data[0]  # グラフの横軸（X軸）
height = cleaned_data[1]  # 値（Y軸）
plt.plot(left, height)
plt.yscale('log')
plt.xscale('log')
plt.show()