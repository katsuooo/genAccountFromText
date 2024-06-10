'''
reciept 2nd parser by template
'''
'''
input - prj_reciept/
'''

from parse_reciept.fileio import fileio
from .deleter import deleter
from .parseRecieptKanFromTemplate import parseRecieptKan
from .parseRecieptKotuKanFromTemplate import parseRecieptKotuKan

prj_dir = 'parse_reciept'
#pre_file_dir = 'pre_parse_reciept\\pre_process'
pre_file_dir = ''
class recieptParser:
    def __init__(self):
        #self.parseAll()
        pass

    def parseAll(self):
        ''' parse all by separate parser
        '''
        fio = fileio(prj_dir)
        deleter(prj_dir)
        #reciept
        reciept = fio.readAll(pre_file_dir)
        parseRecieptKan(reciept, prj_dir)
        #reciept-kotu
        reciept_kotu = fio.readKotuAll()
        parseRecieptKotuKan(reciept_kotu, prj_dir)
    
    def fileClear(self, path):
        # gen file clear
        deleter(path)

    def readAllIntermediate(self, path):
        #中間ファイルの全読み込み
        fio = fileio(prj_dir)
        return fio.readAllIntermediate(path)
    
    def getJsonList(self, path, fList):
        #file-listをパースしpathに保存
        return parseRecieptKan(reciept, prj_dir)





if __name__ == prj_dir + '.reciept_kan_templater_main':
    #deleter(prj_dir)
    #input()
    #recieptParser()
    pass