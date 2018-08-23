#-------------------------------------------------------------------------------
# Name:        paper.py
# Purpose:     idontwannawork
# Created:     06/07/2018
# Licence:     MIT licence
#-------------------------------------------------------------------------------
from docx import Document
from docx.shared import Inches
from janome.tokenizer import Tokenizer
import collections

def main():
    #読み込みたいdocxを指定
    document = Document("hoge.docx")
    txt = ""
    delspace = str.maketrans({' ' : None, '　' : None, '\t' : None})
    for para in document.paragraphs:
        txt += para.text.translate(delspace)
    #形態素解析
    t = Tokenizer("userdic.csv", udic_enc="utf8", mmap=True)
    tokens = t.tokenize(txt)
    #出現回数カウント
    tokenlist = [(token.base_form,token.part_of_speech) if '名詞' in token.part_of_speech else ('***名詞以外***', '') for token in tokens]
    c = collections.Counter(tokenlist)
    for out in c.most_common() :
        print(out[0][0] + ',' + out[0][1] + ',' + str(out[1]))
    print('--------------------名詞以外--------------------')
    for token in tokens :
        if not '名詞' in token.part_of_speech :
            print(token)
if __name__ == '__main__':
    main()
