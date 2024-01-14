''' kousai-hi input'''
'''
交通費つき
場所がファイル単位でわかれていない。
kotuConfigになんらかの情報をいれる

>>>これ、singleでないほうがいいよね。
bookにいれるか。

>>>場所ごとにファイル化されてないので、bookにはいけないかな。
singleでかいてみる。
'''
'''
default_placeは umedaにしておく
　"SINGLE_KOUSAI": "UMEDA",
'''
'''
4項目のメモはあれば、メモにアペンドする
'''

from .fileIo import fileIo
from .inputsUtil import inputsUtil

class singleKousai:
    def __init__(self, fname, jd):
        '''jd = [line1, line2, ...]'''
        self.toJson(fname, jd)
    def getDefaultPlaceKousai(self, fname):
        '''ファイルのデフォルト場所を得る
           交際費に場所つきのデータ用
           fnameを_で区切り末尾を場所情報とする
        '''
        x = fname.split('_')
        return x[len(x)-1].upper()
    def parse(self, fname, lines, fio):#
        '''text linesのパース'''
        '''lines
        [m/d, xxxx(val), place, memo or none]
        '''
        iu = inputsUtil()
        newd = []
        newKotu = []
        myPlace = self.getDefaultPlaceKousai(fname)
        for line in lines:
            #myPlace = iu.getDefaultPlaceKousai(fname)   
            print(fname, line)
            items = line.split(' ')
            date = items[0]
            val = int(items[1])
            if len(items) > 3:
                memo = items[2] + '-' + items[3]
            elif len(items) > 2:
                memo = items[2]
            else:
                fn = fname.split('_')
                memo = fn[len(fn)-1]
            newd.append(iu.parseBuy(date,val,memo))
            ''' 場所はファイル名からとるのでここはパス
            if ('hook' in items[2]) | ('HOOK' in items[2]):
                #hookの場合、飲食で交通費は発生しない
                myPlace = 'NO_KOTU'
            else:
                myPlace = iu.getSpecificPlace(items[2])
            '''
            newKotu.append(iu.parseKotu(date,myPlace,memo))
        fio.saveInputs(newd, fname)
        fio.saveInputsKotu(newKotu, fname)
    def toJson(self, fname, kousaiJson):
        '''text >>> json'''
        fio = fileIo()
        self.parse(fname, kousaiJson, fio)