"""
第4章: 形態素解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt

https://qiita.com/musaprg/items/9a572ad5c4e28f79d2ae

https://kids.gakken.co.jp/jiten/2/20003980.html
"""
# import CaboCha
import MeCab

def get_neko_text():
    with open("chapter4/neko.txt") as f:
        return f.read()

def parse_neko_text():
    with open("chapter4/neko.txt.mecab", mode='w') as output_file:
        data = get_neko_text()
        mecab = MeCab.Tagger()
        parse = mecab.parse(data)
        output_file.write(parse)


parse_neko_text()

# https://pypi.org/project/mecab-python3/
# c = CaboCha.Parser()

# pip freeze > requirements.txt

