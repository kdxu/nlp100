'''
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

# https://qiita.com/ayuchiy/items/c3f314889154c4efa71e#python%E3%81%8B%E3%82%89%E4%BF%82%E3%82%8A%E5%8F%97%E3%81%91%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AB%E8%A7%A6%E3%82%8C%E3%81%A6%E3%81%BF%E3%82%8B

import CaboCha
from pre40 import get_neko_cabocha_lines, get_parse_neko_trees, store_parse_neko_trees
from q40 import get_Morph_list, Morph

class Chunk:
    def __init__(self):
        self.morphs = [] # Morph Object のリスト
        self.srcs = [] # インデックス番号のリスト
        self.dst = -1 # インデックス
        
    def __str__(self):
        sentence = ''
        for morph in self.morphs:
            sentence += str(morph)
        return 'sentence={}, srcs={}, dst={}'.format(sentence, self.srcs, self.dst)

# store_parse_neko_trees()
trees = get_neko_cabocha_lines()

# アスタリスクからはじまる行が係り受けの先を表している？
def gen_chunks():
    chunk_dict = dict()
    srcs = []
    dst = -1
    for tree in trees:
        # 一文に対して、 Chunk のリスト
        # 全体 (key, [Chunk])
        # 一文の終了判定
        if tree == 'EOS\n':
            print('EOS!')
            print('index list=', srcs)
            srcs = []
        # 先頭が*の行は係り受け解析結果
        elif tree[0] == '*':
            # * 0 2D 0/1 -0.217773
            # * 1 2D 0/2 -0.217773
            # * 2 -1D 0/2 0.000000
            # EOS!
            # 空白で区切る
            splitted_tree = tree.split(' ')
            dst = splitted_tree[1]
            srcs.append(int(dst))
            print('係り受け解析結果 {}, dst ={}'.format(tree, dst))
        else:
            chunk = Chunk()
            chunk.morphs = [Morph('surface', 'base', 'pos1', 'pos2')] # ??
            # chunk_list.append(Chunk)

# 名前は---D
#     まだ-D
#     無い。

    # 吾輩は---------D
    #   ここで-D     |
    #     始めて-D   |
    #   人間という-D |
    #         ものを-D
    #           見た。

gen_chunks()
#print(trees[:50])
# len(trees)
#print(len(trees))
# print(trees[0]) #.toString(CaboCha.FORMAT_TREE))

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
