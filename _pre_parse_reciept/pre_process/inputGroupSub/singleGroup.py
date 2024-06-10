'''単独処理が必要なtext'''
'''
yachin - 振込日のみだが月末に発生。振込忘れは未払い。火災保険は不定期に。
library - 交通費のみ
zappi - u=uriKakekin >>> サフィックスで切り替えるのでシングルへ
'''

from .inputsUtil import inputsUtil
from .fileIo import fileIo
import copy
from .singleKousai import singleKousai
from .singleParseNoKotu import singleParseNoKotu
from .singleYachin import singleYachin
from .singleZappi import singleZappi
from .suidouKounetsu import suidouKounetsu
from .singleTuhan import singleTuhan


class singleGroup:
    def __init__(self):
        self.iu = inputsUtil()
    def getDefaultPlace(self, fname):
        '''ファイル毎のデフォルトの場所を得る'''
        return self.iu.getDefaultPlace(fname)
    def saveKotu(self, jd, fname):
        '''jsonInputsKotuに保存'''
        fio = fileIo()
        fio.saveInputsKotu(jd, fname)
    def libraryToJson(self, fname, j):
        '''j = [m/d, m/d,....]
        交通費用データをつくる
        '''
        libPlace = self.getDefaultPlace(fname.upper())
        base = self.iu.getBase()
        newl = []
        for x in j:
            jd = copy.deepcopy(base)
            jd['date'] = x
            jd['memo'] = 'library'
            jd['place'] = libPlace
            newl.append(jd)
        self.saveKotu(newl, fname)
    def toJson(self, singlesJ):
        ''' text to json '''
        for fname in singlesJ:
            if fname == 'single_library':
                self.libraryToJson(fname, singlesJ[fname])
            elif 'single_kousai' in fname:
                singleKousai(fname, singlesJ[fname])
            elif fname == 'single_nizukuri':
                singleParseNoKotu(fname, singlesJ[fname])   
            elif fname == 'single_ryohi':
                singleParseNoKotu(fname, singlesJ[fname])   
            elif fname == 'single_ryohi_room':
                singleParseNoKotu(fname, singlesJ[fname])   
            elif fname == 'single_ryohi_taxi':
                singleParseNoKotu(fname, singlesJ[fname])   
            elif fname == 'single_ryohi_shin_kan_sen':
                singleParseNoKotu(fname, singlesJ[fname])   
            elif fname == 'single_yachin':
                print(singlesJ[fname])
                singleYachin(fname, singlesJ[fname])               
            elif fname == 'single_uriage':
                singleParseNoKotu(fname, singlesJ[fname])    
            elif fname == 'single_gaichukouchin':
                singleParseNoKotu(fname, singlesJ[fname])  
            elif 'single_zappi' in fname:
                singleZappi(fname, singlesJ[fname])  
            elif 'single_suidoukonetsu' in fname:
                suidouKounetsu(fname, singlesJ[fname])
            elif 'single_tuhan' in fname:
                singleTuhan(fname, singlesJ[fname])
