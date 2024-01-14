''' inputs utility '''


from .choDio import choDio
import copy
from datetime import date
from dateutil.relativedelta import relativedelta

class inputsUtil:
    def __init__(self):
        cd = choDio()
        self.inputsConfig = cd.getConfig('inputs')  
    def getInputConfig(self):
        return self.inputConfig      
    def getDefaultPlace(self, fname):
        '''ファイルのデフォルト場所を得る'''
        print(fname, fname.upper())
        return self.inputsConfig['default_place'][fname.upper()]
    def getSpecificPlace(self, placeKey):
        '''ファイルの指定の場所を得る'''
        return self.inputsConfig['places'][placeKey.upper()]
    def getBase(self):
        '''inputsConfig/json_base'''
        return self.inputsConfig["JSON_BASE"]
    def parseBuy(self, mydate, val, fname):
        '''購入クエリ'''
        jd = copy.deepcopy(self.getBase())
        jd['date'] = mydate
        jd['val'] = val
        jd['place'] = ''
        jd['memo'] = fname
        return jd
    def parseKotu(self, mydate, place, fname):
        '''交通費クエリ'''
        '''valはplaceから後処理でいれる'''
        jd = copy.deepcopy(self.getBase())
        jd['date'] = mydate
        jd['val'] = ''
        jd['place'] = place
        jd['memo'] = fname
        return jd
    def getYachin(self):
        '''yachin返す'''
        cd = choDio()
        #config = cd.getConfig('cho2019')
        config = cd.getConfig('cho')
        return config['yachin']
    def getYear(self):
        '''西暦年返す'''
        cd = choDio()
        #config = cd.getConfig('cho2019')
        config = cd.getConfig('cho')
        return config['year']
    def getLaseMonthsMatsubi(self, mydate):
        '''dateの前月の末尾をえる'''
        thisYear = int(self.getYear())
        items = mydate.split('/')
        thisMonth = int(items[0])
        thisFirstDate = date(thisYear, thisMonth, 1)
        zengetuLastDay = thisFirstDate - relativedelta(days=1)
        mdStr = str(zengetuLastDay.month) + '/' + str(zengetuLastDay.day)
        return mdStr
