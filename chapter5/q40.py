'''
第5章: 係り受け解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
import CaboCha

def __init__(self, hoge, huga):
    self.hoge = hoge
    
'''

import CaboCha

def get_neko_lines():
    with open("chapter4/neko.txt") as f:
        return f.readlines()

def get_parse_neko_text():
    c = CaboCha.Parser()
    sentences = get_neko_lines()
    with open("chapter5/neko.txt.cabocha", mode='w') as output_file:
        for sentence in sentences:
            tree = c.parse(sentence)            
            output_file.write(tree.toString(CaboCha.FORMAT_LATTICE))

get_parse_neko_text()
# あと    名詞,一般,*,*,*,*,
# あと,アト,アト
# surface TAB pos,pos1,x,x,x,x,base,x,x
# * 0 2D 0/0 -0.764522 (具体的には, アスタリスクで始まる文節の開始位置を意味する行が追加されます。アスタリスクの後には, 文節番号 (0から始まる整数),係り先番号 (係り先は同定されていないので常に -1) が続きます。)
# EOS
# def __str__(self):

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface={0},base={1},pos={2},pos1={3}'.format(self.surface, self.base,self.pos,self.pos1)

def get_neko_cabocha_lines():
    with open("chapter5/neko.txt.cabocha") as f:
        return f.readlines()

result = []
for line in get_neko_cabocha_lines():
    if line.startswith("*") or line.startswith("EOS"):
        continue
    
    l1 = line.split("\t")
    surface = l1[0]
    l2 = l1[1].split(",")
    pos = l2[0]
    pos1 = l2[1]
    base = l2[6]
    result.append(Morph(surface,base,pos,pos1))

print(result[2])