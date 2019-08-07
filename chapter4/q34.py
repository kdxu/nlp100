'''
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
'''

from q30 import parse_neko_text_list
list = parse_neko_text_list()

result = [list[i-1]['surface'] + item['surface'] + list[i+1]['surface'] for i, item in enumerate(list) if list[i-1]['pos'] == '名詞' and item['pos1'] == '連体化' and list[i+1]['pos'] == '名詞']

print('\n'.join(map(str, result[:200])))