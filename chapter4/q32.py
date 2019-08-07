'''
32. 動詞の原形
動詞の原形をすべて抽出せよ．
'''

from q30 import parse_neko_text_list
list = parse_neko_text_list()
result = [item['base'] for item in list if item['pos'] == '動詞' ]

print('\n'.join(map(str, result[:20])))