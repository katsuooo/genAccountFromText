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

class parseRecieptKan:
    def __init__(self, filesJson, prj_dir):
        self.prj_dir = prj_dir
        self.recieptKan = []
        temp = templater()
        self.parseFiles(filesJson)
    def parseByTemplate(self, jd, template):
        '''jdlistはone file json dict'''
        x = copy.deepcopy(template)
        ku = kanUtil(self.prj_dir)
        x['date'] = ku.setKanDate(jd['date'])
        x['val'] = jd['val']
        x['memo'] = jd['memo']
        self.recieptKan.append(x)
    def parse(self, fname, jd):
        '''jdはdict'''
        '''jdはfile list'''
        t = templater()
        template = t.getTemplateByFname(fname)
        print(fname, template)
        self.recieptKan = []
        #print(fname)
        for x in jd:
            self.parseByTemplate(x, template)
        fio = fileio(self.prj_dir)
        fio.saveKan(self.recieptKan, fname)
    def parseFiles(self, filesJson):
        for key in filesJson:
            self.parse(key, filesJson[key])