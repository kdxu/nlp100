"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki API(https://www.mediawiki.org/wiki/API:Main_page/ja)のimageinfo(https://www.mediawiki.org/wiki/API:Properties/ja#imageinfo_.2F_ii)を呼び出して，ファイル参照をURLに変換すればよい）
"""

"""
get_imageinfo.py

#!/usr/bin/python3

    get_imageinfo.py

    MediaWiki Action API Code Samples
    Demo of `Imageinfo` module: Get information about 
    an image file.
    MIT license
# from https://www.mediawiki.org/wiki/API:Imageinfo

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "titles":"File:Billy_Tipton.jpg",
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
"""

# ('国旗画像', 'Flag of the United Kingdom.svg')
# requests: https://requests-docs-ja.readthedocs.io/en/latest/

import requests

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"

PARAMS = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "titles": "File:Flag of the United Kingdom.svg",
    "iiprop": "url",
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
# https://jsonformatter.curiousconcept.com/
url = DATA['query']['pages']['-1']['imageinfo'][0]['url']
print(url)

# python3 -m venv .
# source bin/activate
# pip install requests
# pip freeze > requirements.txt
# pip install -r requirements.txt
# deactivate

# https://github.com/github/gitignore/blob/master/Global/VirtualEnv.gitignore
