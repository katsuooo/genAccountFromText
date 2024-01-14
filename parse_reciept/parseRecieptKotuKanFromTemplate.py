'''
reciept-kotu
templateをベースに変換する

prj_reciept/intermediate_json_kotu
book, kaigi, shoumouhin >>> ファイル名待つのplaceにより、交通費を自動付加
library >>> 自動的に図書館往復の交通費を付加(西長堀)
kousai  >>> クエリ内shopにより、場所をテンプレートに記載して自動付加
'''
from .templaterKotu import templater
import copy
from .fileio import fileio
from .kanUtil import kanUtil

class parseRecieptKotuKan:
    def __init__(self, filesJson, prj_dir):
        self.prj_dir = prj_dir
        self.recieptKan = []
        temp = templater()
        self.parseFiles(filesJson)
    def parseByTemplate(self, jd, template):
        '''jdlistはone file json dict'''
        x = copy.deepcopy(template)
        ku = kanUtil()
        x['date'] = ku.setKanDate(jd['date'])
        #x['val'] = jd['val']
        x['memo'] = jd['memo']
        self.recieptKan.append(x)
    def parse(self, fname, jd):
        '''jdはdict'''
        '''jdはfile list'''
        t = templater()
        self.recieptKan = []
        for x in jd:
            if x['place'] == 'NO_KOTU':
                continue
            template = t.getTemplateByPlace(x['place'])
            if template != 'NO_KOTU':
                self.parseByTemplate(x, template)
        fio = fileio(self.prj_dir)
        fio.saveKotuKan(self.recieptKan, fname)
    def parseFiles(self, filesJson):
        for key in filesJson:
            self.parse(key, filesJson[key])