'''
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
'''

# https://note.nkmk.me/python-list-index/

from q30 import parse_neko_text_list
list = parse_neko_text_list()

result = [item['surface'] for item in list if item['pos1'] == 'サ変接続' ]
#result2 = [(i, item) for i,item in enumerate(list) if item['base'] == '*\n' ]

'''
('——', '*\n')
頸筋
https://www.aozora.gr.jp/cards/000148/files/789_14547.html
'''
#print('\n'.join(map(str, list[1710:1760])))

print('\n'.join(map(str, result[:50])))

