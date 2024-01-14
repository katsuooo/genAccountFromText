'''chobo data interface
データはfile, mongo
アプリからは、file,dbを意識しない風に

input data
textファイルから入力。5つのグループにわける
- group -
book
kaigi
dc
risona
extendables
'''

from .fileIo import fileIo
from .intermediateGroup import intermediateGroup
class choDio:
    def __init__(self):
        self.fio = fileIo()
        self.img = intermediateGroup()
    '''
    def getChoConfig(self):
        chobo config の取得
        return self.choConfig
    '''
    def getConfig(self, name):
        '''name+'Config'.jsonをかえす'''
        fpath = ['config_json', name + 'Config']
        return self.fio.readJson(fpath)
    '''
    def getInputGroupList(self, category):
        input groupのメンバリストを得る
        return self.ig.getInputGroupList(category)
    '''
    def getInputText(self, inputName):
        '''inputNameのテキストを返す'''
        return self.fio.readInputText(inputName)
    def saveKotu(self, jd, label):
        '''restore kotu(intermediatekotu)'''
        self.fio.saveIntermediateKotu(jd, label)
    def getIntermediateKotuAll(self):
        '''中間ファイルkotuのリストを返す
        データを読み込み、全部をdict配列で渡す。
        '''
        return self.img.getIntermediateKotuAll()
    '''
    def getInputGroupAll(self, group):
        input groupのtextをdictで返す
        return self.ig.getInputGroup(group)
    '''
    '''
    def saveKotu(self, jd):
        formatted kotuを保存
        fpath = ['jsonOutputKotu', 'kotu']
        self.fio.writeJson(jd, fpath)
    '''
    def storeFormattedKotu(self, jd):
        '''勘定フォーマットされた交通費の保存'''
        #fpath = ['jsonOutputKotu', 'kotu']
        fpath = ['out_json_kotu', 'kotu']
        self.fio.writeJson(jd, fpath)