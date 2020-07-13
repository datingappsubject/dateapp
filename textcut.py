from ckiptagger import WS, POS, NER
import tensorflow
import tkinter as tk
import re

def remove(text):
    remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’；：（）！[\\]^_`{|}~\n]+'
    return re.sub(remove_chars, '', text)

f = open("新聞稿.txt",mode='r',encoding="utf-8")
text=f.readlines()
text=''.join(text)
text=remove(text)

ws = WS("./data")
#pos = POS("./data")
#ner = NER("./data")

ws_results = ws([text])
#pos_results = pos(ws_results)
#ner_results = ner(ws_results, pos_results)
print(type(ws_results))

#print(pos_results)
#for name in ner_results[0]:
 #   print(name)


str1=''.join(str(v) for v in ws_results)

newtext = open ("output.txt","w")
for i in ws_results:
    for j in i :
        newtext.write(j)
        newtext.write('-'+str(str1.count(j)))
        newtext.write('\n')
newtext.close()

