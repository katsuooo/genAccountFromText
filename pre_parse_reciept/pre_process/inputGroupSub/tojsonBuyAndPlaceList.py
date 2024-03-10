'''
レシートテキストのパース

交通費は勘定ではなく、day - place配列 のリストを作成
交通費クエリ作成用の情報ファイルをまず作成する。

'''

from .fileIo import fileIo
from .inputsUtil import inputsUtil
import copy

class tojsonBuyAndPlaceList:
    def __init__(self):
        self.fio = fileIo()
    def getPlace(self, fname):
        '''ファイル名から場所を取得'''
        '''_連結の最終文字列が場所'''
        '''場所がリストに含まれない場合はNO_KOTU'''
        allPlace = self.fio.getStationList()
        items = fname.split('_')
        place = items[len(items)-1]
        if place in allPlace:
            return place
        return 'NO_KOTU'
    def parse(self, fname, lines):
        '''text linesのパース'''
        iu = inputsUtil()
        #myPlace = iu.getDefaultPlace(fname)
        myPlace = self.getPlace(fname)
        newd = []
        newKotu = []
        placeInfo = []
        for line in lines:
            line = line.replace('　',' ')
            items = line.split(' ')
            date = items[0]
            if '+' in items[1]:
                num = items[1].split('+')
                sum = 0
                for i in num:
                    sum += int(i)
                items[1] = sum
            val = int(items[1])
            if len(items) > 2:
                memo = items[2] + '__' + fname
            else:
                memo = fname
            newd.append(iu.parseBuy(date,val,memo))
            if myPlace != 'NO_KOTU':
                newKotu.append(iu.parseKotu(date,myPlace,fname))
                placeInfo.append({date:{"place": myPlace, "memo": fname}})
        if newd != []:
            self.fio.saveInputs(newd, fname)
        if newKotu != []:
            self.fio.saveInputsKotu(newKotu, fname)
        if placeInfo != []:
            self.fio.savePlaceInfo(placeInfo, fname)

    def toJson(self, inputGroupJson):
        '''text >>> json
        kaigi,shoumouhin,bookの項目毎にまとまったデータが届く
        '''
        for fname in inputGroupJson:
            self.parse(fname, inputGroupJson[fname])