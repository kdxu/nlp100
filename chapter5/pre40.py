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

def get_neko_cabocha_lines():
    with open("chapter5/neko.txt.cabocha") as f:
        return f.readlines()
    
plist = []

def get_parse_neko_trees():
    sentences = get_neko_lines()
    with open("chapter5/neko.txt.cabocha", mode='w') as output_file:
        trees = []
        for sentence in sentences:
            parser = CaboCha.Parser()
            tree = parser.parse(sentence)            
            trees.append(tree)
            plist.append(parser)
        return trees

"""
def parse(sentences):
    trees = []
    plist = []
    for s in sentences:
        parser = CaboCha.Parser()
        trees.append(parser.parse(s))
        plist.append(parser)
"""