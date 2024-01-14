'''銀行他のtext to json'''
'''
risona1,2
旅費
荷造運賃
通信費(dc除く分)
消耗品a4(通販分)
>>> risona2のみになった
'''
'''
# r: 利息 
# u: 売上
['2/9 1 r 利息31-2-8まで', '3/15 39136 u 豊永産業アンプ基板修理'] <class 'list'>

date: m/d
val : xxx
command : r
memo : text str


'''
'''
1とinputの形態が違いすぎていっしょにならない。
勘定の判定部(recieptRisona)のみ共用する。
jsonファイルは
risona1 -> jsonIntermediateReciept
risona2 -> jsonInputs
になるか。

jsonInputsはすごく冗長だが、、、
それならrecieptRisonaは
jsonInputs >>> jsonIntermediate
の間で使用することになるでしょう。
'''
'''
ではなく、仕分けはここでやる。
仕分け結果をファイル種をかえて保存する方法。
または、recieptにもっていってパースするか。
jsonReciept/rough_rison2.jsonにするか。
>>> 下にする
ここでゆるくパースしているのでrough_をとったファイル名にする。
risona_risona2.jsonでいくか。
'''

import copy
from .fileIo import fileIo


class risonaGroup:
    def __init__(self):
        pass
    def parseRisona2(self, textList, fname):
        risonas = []
        for line in textList:
            items = line.split(' ')
            risonaJson = {}
            risonaJson['date'] = items[0]
            risonaJson['val'] = int(items[1])
            risonaJson['command'] = items[2]
            risonaJson['memo'] = items[3]
            risonas.append(copy.deepcopy(risonaJson))
        fio = fileIo()
        fio.saveReciept(risonas, fname)        
    def toJson(self, jd):
        for key in jd:
            self.parseRisona2(jd[key], key)
