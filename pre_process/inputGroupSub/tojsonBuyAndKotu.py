''' buyとkotuのjson入力データを生成'''
'''適応する入力group
kaigi group
shoumouhin group
book group
'''

from .fileIo import fileIo
from .inputsUtil import inputsUtil
import copy

class tojsonBuyAndKotu:
    def __init__(self):
        #self.iu = inputsUtil()
        pass
    def parse(self, fname, lines, fio):#
        '''text linesのパース'''
        iu = inputsUtil()
        myPlace = iu.getDefaultPlace(fname)
        newd = []
        newKotu = []
        for line in lines:
            items = line.split(' ')
            date = items[0]
            val = int(items[1])
            if len(items) > 2:
                #memo = items[2] + '__' + fname
                memo = items[2]
            else:
                memo = fname
            newd.append(iu.parseBuy(date,val,memo))
            if myPlace != 'NO_KOTU':
                newKotu.append(iu.parseKotu(date,myPlace,fname))
        if newd != []:
            fio.saveInputs(newd, fname)
        if newKotu != []:
            fio.saveInputsKotu(newKotu, fname)
    def toJson(self, inputGroupJson):
        '''text >>> json'''
        fio = fileIo()
        for fname in inputGroupJson:
            self.parse(fname, inputGroupJson[fname], fio)