"""
 20. JSONデータの読み込み
 1行に1記事の情報がJSON形式で格納される
 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
 Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
 json: https://docs.python.org/ja/3/library/json.html
 in: https://docs.python.org/3/reference/expressions.html#membership-test-details

"""

import json
def get_uk_article():
        with open("chapter3/jawiki-country.json") as f:
        lines = f.readlines()
        articles =  [json.loads(line) for line in lines]
        article = [article for article in articles if -1 < article['title'].find('イギリス')]
        return article[0]['text']
        