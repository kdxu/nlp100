"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
他との区別（斜体）	''他との区別''
強調（太字）		'''強調'''
斜体と強調	'''''斜体と強調'''''
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
"""
from q25 import get_basic_info
import re

key_value = get_basic_info()
result = [(key, re.sub(r'\'\'+', '', value)) for (key, value) in key_value]
print('\n'.join(map(str, result)))
# https://uxmilk.jp/8662