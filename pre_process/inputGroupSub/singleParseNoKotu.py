''' nizukuri input '''
'''
交通費なし
nizukuri: 荷造運賃-事業主借
ryohi   : 旅費交通費
uriage  :
gaichu-kouchin:
'''
'''
旅費交通費は、一度自動交通費データをミックスされるため、
output_json_placeに保存する。
'''

from .fileIo import fileIo
from .inputsUtil import inputsUtil

class singleParseNoKotu:
    def __init__(self, fname, jd):
        '''jd = [line1, line2, ...]'''
        self.toJson(fname, jd)
    def parse(self, fname, lines):
        '''text linesのパース'''
        '''lines
        [m/d, xxxx(val), place, memo or none]
        '''
        fio = fileIo()
        iu = inputsUtil()
        newd = []
        for line in lines:
            items = line.split(' ')
            date = items[0]
            val = int(items[1])
            if len(items) > 3:
                memo = items[2] + '-' + items[3]
            elif len(items) > 2:
                memo = items[2]
            else:
                memo = ''
            newd.append(iu.parseBuy(date,val,memo))
        fio.saveInputs(newd, fname)
    def toJson(self, fname, noKotuJson):
        '''text >>> json'''
        self.parse(fname, noKotuJson)