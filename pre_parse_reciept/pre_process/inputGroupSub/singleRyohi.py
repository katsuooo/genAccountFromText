''' ryohi input
    自動添付交通費はつけない
'''

from .fileIo import fileIo
from .inputsUtil import inputsUtil

class singleRyohi:
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
        for line in lines:
            items = line.split(' ')
            date = items[0]
            val = int(items[1])
            if len(items) > 3:
                memo = items[2] + '-' + items[3]
            else:
                memo = items[2]
            newd.append(iu.parseBuy(date,val,memo))
        fio.saveInputs(newd, fname)
    def toJson(self, fname, ryohiJson):
        '''text >>> json'''
        fio = fileIo()
        self.parse(fname, ryohiJson, fio)