''' uriage input '''
'''
交通費なし
売掛金 - 売上高
'''

class singleUriage:
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