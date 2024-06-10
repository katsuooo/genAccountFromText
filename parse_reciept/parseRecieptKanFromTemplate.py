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
        #t = templater()
        #template = t.getTemplateByFname(fname)
        template = self.templater.getTemplateByFname(fname)
        self.recieptKan = []
        for x in jd:
            self.parseByTemplate(x, template)
        #fio = fileio(self.prj_dir)
        #fio.saveKan(self.recieptKan, fname)
        return copy.deepcopy(self.recieptKan)

    def parseFiles(self, filesJson):
        for key in filesJson:
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