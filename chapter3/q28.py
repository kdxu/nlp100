"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""
import re
from q27 import get_cleaned_data

data = get_cleaned_data()

# print('\n'.join(map(str, data)))

# <ref>.*</ref>
# br
pattern = re.compile(r'''
                     <
                     \/?
                     [br|ref]
                     [^>]*?
                     >
                     ''', re.MULTILINE + re.VERBOSE)

# [http://xxxx bb]
# <a href='http://xxx'>bb</a>
res = [(key, pattern.sub('', value)) for (key, value) in data]
# print('\n'.join(map(str, res)))

pattern2 = re.compile(r'''
                      \[http:\/\/
                      (?:
                        [^\s]*?
                        \s
                      )
                      ([^\]]*?)
                      \]
                     ''', re.MULTILINE + re.VERBOSE)

res2 = [(key, pattern2.sub(r'\1', value)) for (key, value) in res]
print('\n'.join(map(str, res2)))

# https://ja.wikipedia.org/wiki/Template:Lang
# {{lang|en|United Kingdom of Great Britain and Northern Ireland}} => United Kingdom of Great Britain and Northern Ireland
# {{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}} => An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath
# TODO Lang タグの抜き出し
pattern3 = re.compile(r'''
                      \{\{lang\|.+\|
                      (.*)
                      \}\}
                      ''', re.MULTILINE + re.VERBOSE)

res3 = [(key, pattern3.sub(r'\1', value)) for (key, value) in res2]
print('\n'.join(map(str, res3)))