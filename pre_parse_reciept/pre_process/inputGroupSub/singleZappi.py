'''
雑費処理

年末の売掛金の振込手数料で引かれた分をまとめて記載
yatin_u 売掛金
'''
from .fileIo import fileIo
from .inputsUtil import inputsUtil

class singleZappi:
    def __init__(self, fname, jd):
        self.zappi_u = []
        self.toJson(fname, jd)
    def fetchCommand(self, items):
        date = items[0]
        command = items[2]
        memo = ''
        iu = inputsUtil()
        '''u コマンド解析'''
        '''ここで解析しない。file名に_uをつけて分類する。'''
        if command == 'u':
            val = int(items[1])
            memo = items[3]
            jd = iu.parseBuy(date,val,memo)
            #self.zappi_u.append(jd)
        elif command == 'r':
            val = int(items[1])
            memo = items[3]
            jd = iu.parseBuy(date,val,memo)
            #self.zappi_u.append(jd)
        elif command == 'm':
            val = int(items[1])
            memo = items[3]
            jd = iu.parseBuy(date,val,memo)
        return jd
    def decoding(self, line):
        ''' line中のコマンド有無、デコードを行う'''
        items = line.split(' ')
        if len(items) < 4:
            print('single-zappi parsing... no-aite-kanjou-simbole')
        else:
            return self.fetchCommand(items)
        return 'NO_DATA'
    def saveJson(self, newd, fname):
        fio = fileIo()
        fio.saveInputs(newd, fname)
    def toJson(self, fname, lines):
        '''txt to json'''
        '''-uは元ファイル名に含める'''
        print('single-zappi-------')
        zappi_u = []
        zappi_r = []
        zappi_m = []
        for line in lines:
            q = self.decoding(line)
            if q != 'NO_DATA':
                command = line.split(' ')[2]
                if  command == 'u':
                    zappi_u.append(q)
                elif command == 'r':
                    zappi_r.append(q)
                elif command == 'm':
                    zappi_m.append(q)
        if len(zappi_u) != 0:
            self.saveJson(zappi_u, fname + '_u')
        if len(zappi_r) != 0:
            self.saveJson(zappi_r, fname + '_r')
        if len(zappi_m) != 0:
            self.saveJson(zappi_m, fname + '_m')

