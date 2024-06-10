'''中間ファイルのリスト関連'''
'''intermediate, intermediateKotu'''


#from pgDio.choDio import choDio

from .fileIo import fileIo

class intermediateGroup:
    def __init__(self):
        self.fio = fileIo()
    def getIntermediateKotuAll(self):
        '''intermediate_kotuフォルダの全ファイルをdict化して返す。
        keyはファイル名
        '''
        fnameList = self.fio.getFileNamesFromFolder('jsonIntermediateKotu')
        all = []
        for f in fnameList:
            text = self.fio.getIntermediateKotu(f)
            all.append({f:text})
        return all
    def getIntermediateKotuDaykeyAll(self):
        '''intermediate_kotu_daykeyフォルダの全ファイルをdict化して返す。
        keyはファイル名
        '''
        fnameList = self.fio.getFileNamesFromFolder('jsonIntermediateKotu')
        all = []
        for f in fnameList:
            text = self.fio.getIntermediateKotuDaykey(f)
            all.append({f:text})
        return all
    def storeKotuMixin(self, mixd):
        '''kotu mixinデータのストア'''
        #fpath = ['jsonOutputKotu', 'kotuAllnoFormat']
        fpath = ['intermediate_json_kotu', 'kotuAllnoFormat']
        self.fio.writeJson(mixd, fpath)
    def getKotuAllnoFormat(self):
        '''kotu all とりだし'''
        #fpath = ['jsonOutputKotu', 'kotuAllnoFormat']
        fpath = ['intermediate_json_kotu', 'kotuAllnoFormat']
        return self.fio.readJson(fpath)