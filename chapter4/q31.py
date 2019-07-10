'''
31. 動詞
動詞の表層形をすべて抽出せよ．
'''

from q30 import parse_neko_text_list

# print(parse_neko_text_list()[:20])
list = parse_neko_text_list()

results = [ item['surface'] for item  in list if item['pos'] == '動詞' ] 

print(results[:20])