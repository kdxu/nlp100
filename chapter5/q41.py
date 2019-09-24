'''
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

# https://qiita.com/ayuchiy/items/c3f314889154c4efa71e#python%E3%81%8B%E3%82%89%E4%BF%82%E3%82%8A%E5%8F%97%E3%81%91%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AB%E8%A7%A6%E3%82%8C%E3%81%A6%E3%81%BF%E3%82%8B

import CaboCha
from pre40 import get_neko_cabocha_lines, get_parse_neko_trees
from q40 import get_Morph_list

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.srcs = srcs
        self.dst = dst

trees = get_parse_neko_trees()
#print(trees[:50])
# len(trees)
#print(len(trees))
print(trees[0].toString(CaboCha.FORMAT_TREE))

# neko_cabocha_list = get_Morph_list()
# # neko_cabocha_list[:50]
# print(neko_cabocha_list[:10])
# print(neko_cabocha_list[1])
# print(neko_cabocha_list[2])
# print(neko_cabocha_list[3])
# print(neko_cabocha_list[4])
# print(neko_cabocha_list[5])
# print(neko_cabocha_list[6])
# print(neko_cabocha_list[7]) cmd + /
# print(tree.toString(CaboCha.FORMAT_LATTICE))