# nlp100

## neko.txt のダウンロード

```shell
$ cd chapter4/
$ wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt
```

## cabocha のインストール

### homebrew の場合

```shell
$ brew install cabocha
```

## pipenv のセットアップ

```shell
$ python3 -V
3.7.1
$ pip3 install pipenv
```

## モジュールのインストール

```shell
$ PIPENV_VENV_IN_PROJECT=1 pipenv install -d
```

## 実行

```shell
$ pipenv run exec chapter1/00.py
```
