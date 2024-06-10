'''
水道光熱費

年末の売掛金の振込手数料で引かれた分をまとめて記載
yatin_u 売掛金
'''
from .fileIo import fileIo
from .inputsUtil import inputsUtil

class suidouKounetsu:
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
            10/5 1606
        '''
        iu = inputsUtil()
        newd = []
        for line in lines:
            items = line.split(' ')
            date = items[0]
            val = int(items[1])
            memo = 'suidou' + items[0]
            newd.append(iu.parseBuy(date,val,memo))
        fio.saveInputs(newd, fname)

    def toJson(self, fname, suidouJson):
        '''text >>> json'''
        fio = fileIo()
        self.parse(fname, suidouJson, fio)

