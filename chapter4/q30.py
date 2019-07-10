'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''
def parse_neko_text_list():
    with open('chapter4/neko.txt.mecab') as f:
        result_list = []
        for line in f:
            cols = line.split('\t')
            if len(cols) < 2:
                break
            detail_cols = cols[1].split(',')
            item = {
                'surface': cols[0],
                'base': detail_cols[6],
                'pos': detail_cols[0],
                'pos1': detail_cols[1]
            }
            result_list.append(item)
            
        return result_list

# print('\n'.join(map(str, parse_neko_text_list()[:20])))