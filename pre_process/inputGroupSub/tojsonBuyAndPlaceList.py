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
    def parse(self, fname, lines, input_config):
        '''text linesのパース'''
        iu = inputsUtil(input_config)
        #myPlace = self.getPlace(fname)
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
            #if myPlace != 'NO_KOTU':
            #    newKotu.append(iu.parseKotu(date,myPlace,fname))
            #    placeInfo.append({date:{"place": myPlace, "memo": fname}})
        if newd != []:
            self.fio.saveInputs(newd, fname)
        #if newKotu != []:
        #    self.fio.saveInputsKotu(newKotu, fname)
        #if placeInfo != []:
        #    self.fio.savePlaceInfo(placeInfo, fname)

    def toJson(self, inputGroupJson, input_config):
        '''text >>> json
        kaigi,shoumouhin,bookの項目毎にまとまったデータが届く
        '''
        for fname in inputGroupJson:
            self.parse(fname, inputGroupJson[fname], input_config)

    def parseList(self, fname, lines, input_config):
        #text linesのパース 交通費データは使用しなくなったので作成しない
        iu = inputsUtil(input_config)
        newd = []
        for line in lines:
            line = line.replace('　',' ')
            items = line.split(' ')
            date = items[0]
            if fname == 'exclude_library':
                #libraryはval 240x2固定
                items.append('480')
            if '+' in items[1]:
                num = items[1].split('+')
                sum = 0
                for i in num:
                    sum += int(i)
                items[1] = sum
            val = int(items[1])
            if len(items) > 2:
                # file名がおかしくなるのでfnameとする
                #memo = items[2] + '__' + fname
                #memo = fname
                memo = items[2]
            else:
                memo = fname
            newd.append(iu.parseBuy(date,val,memo,fname))
            #if myPlace != 'NO_KOTU':
            #    newKotu.append(iu.parseKotu(date,myPlace,fname))
            #    placeInfo.append({date:{"place": myPlace, "memo": fname}})
        if len(newd) == 0:
            print('newd = 0!!!!!!!!!!!!!!!!',newd, len(newd), fname)
        return newd

    def getJsonList(self, inputGroupJson, input_config):
        '''text >>> jsonのリストを得る
        kaigi,shoumouhin,bookの項目毎にまとまったtextをjsonのlistに変換
        '''
        jlist = []
        for fname in inputGroupJson:
            print(fname)
            newd = self.parseList(fname, inputGroupJson[fname], input_config)
            if len(newd) != 0:        
                #query sample -> [{'date':'3/14','val':320',place':'','memo':'kaigi_break_nagahori ','fname':'kaigi_break_nagahori '}, ...]
                jlist.append(newd)
            #raise ValueError('input fileのデータが0です', fname)
        return jlist