
# 開発環境
## Python実行環境
Anacondaがあれば問題なし。もちろん標準パックでもOK。

## エディタ
お気に入りのIDEで。[Pycharm](https://www.jetbrains.com/pycharm/)とか[Atom](https://atom.io/)あたりがやっぱりポピュラーだろうか。個人的には[VSCode](https://code.visualstudio.com/)が軽くて好き。

## 形態素解析
[Janome](http://mocobeta.github.io/janome/)

    $ pip install janome

### NEologd 辞書を内包した janome
[NEologd 辞書を内包した janome をビルドする方法](https://github.com/mocobeta/janome/wiki/(very-experimental)-NEologd-%E8%BE%9E%E6%9B%B8%E3%82%92%E5%86%85%E5%8C%85%E3%81%97%E3%81%9F-janome-%E3%82%92%E3%83%93%E3%83%AB%E3%83%89%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)

ビルド済みパッケージから導入

    $ pip install Janome-0.3.6.neologd-20180409.tar.gz --no-compile

[mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)は、多数のWeb上の言語資源から得た新語を追加することでカスタマイズした[MeCab](http://taku910.github.io/mecab/)
用のシステム辞書。速度は遅いが、より正確に分解してくれる。

## Word読込
[python-docx](https://python-docx.readthedocs.io/en/latest/)

    $ pip install python-docx

docx形式のみ読込可能（docは不可）。一番モダンなため採用。
