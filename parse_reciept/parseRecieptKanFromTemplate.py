'''
reciept
templateをベースに変換する

template 種類 / book, kaigi, shoumouhin, 
 single / gaichuukouchin, kousai, nizukuri, ryohi, uriage, zappi_u 
 yachin / m, oh, om
'''
from .templater import templater
import copy
from .fileio import fileio
from .kanUtil import kanUtil
import copy

class parseRecieptKan:
    '''
    def __init__(self, filesJson, prj_dir):
        self.prj_dir = prj_dir
        self.recieptKan = []
        temp = templater()
        #self.parseFiles(filesJson)
        '''
    def __init__(self,templater):
        self.templater = templater
        self.reciptKan = []

    def parseByTemplate(self, jd, template):
        '''jdlistはone file json dict'''
        x = copy.deepcopy(template)
        ku = kanUtil(self.prj_dir)          #>>>>> date変換にyearを取得するのにconfigのパスが必要。yearわたす？
        x['date'] = ku.setKanDate(jd['date'])
        x['val'] = jd['val']
        x['memo'] = jd['memo']
        self.recieptKan.append(x)
        #return x

    def parse(self, fname, jd):
        '''jdはdict'''
        '''jdはfile list'''
        template = self.templater.getTemplateByFname(fname)
        self.recieptKan = []
        for x in jd:
            self.parseByTemplate(x, template)
        return copy.deepcopy(self.recieptKan)

    def parseTax(self, fname, jd):
        '''消費税勘定'''
        '''消費税は２つクエリを生成  日付処理ができないので、ここでは1つにする？'''
        self.recieptKan = []
        #template = self.templater.getTemplateByFname(fname + '_s')  #消費税発生
        #for x in jd:
        #    self.parseByTemplate(x, template)
        template = self.templater.getTemplateByFname(fname + '_h')  #消費税支払い
        for x in jd:
            self.parseByTemplate(x, template)
        return copy.deepcopy(self.recieptKan)
       

    def parseFiles(self, filesJson):
        for key in filesJson:
            if key == 'tax':
                '''消費税は２組のクエリを生成'''
                self.parseTax(key, filesJson[key])
            else:
                self.parse(key, filesJson[key])
    
    def parseByTemplateWithYear(self,jd, template, year):
        x = copy.deepcopy(template)
        ku = kanUtil(year)  #>>>>> date変換にyearを取得するのにconfigのパスが必要。yearわたす？
        x['date'] = ku.setKanDateWithYear(jd['date'],year)
        x['val'] = jd['val']
        x['memo'] = jd['memo']
        self.recieptKan.append(x)
    
    def parsePerFile(self,fname,jd,year,template):
        '''year, templateを引数からとる'''
        self.recieptKan = []
        for x in jd:
            self.parseByTemplateWithYear(x, template, year)
        return copy.deepcopy(self.recieptKan)