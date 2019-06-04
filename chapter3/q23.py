"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
https://ja.wikipedia.org/wiki/Help:%E3%82%BB%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3
http://www.tohoho-web.com/python/operators.html
+a            # 正数
-a            # 負数
a + b         # 加算
a - b         # 減算
a * b         # 乗算
a / b         # 除算 5 / 2  = 2.5
a % b         # a を b で割った余り
a ** b        # a の b 乗   
a // b        # 切り捨て除算　5 // 2 = 2

strip
https://uxmilk.jp/12804
"""
import re
import q20

uk_article = q20.get_uk_article()
# print(uk_article)

pattern = re.compile(r'^=.*', re.MULTILINE)

result = pattern.findall(uk_article)

levels = [(section.strip('=').strip(), section.count('=') // 2 - 1) for section in result]

print(levels)