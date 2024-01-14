'''
kan_template.json interface
>>> change json to hjson
'''
import json
import hjson
import pathlib

class templater:
    def __init__(self):
        self.template = self.readTemplate()
    def readTemplate(self):
        '''templete.jsonを読み込み'''
        #x = pathlib.Path(__file__).parent
        x = pathlib.Path(__file__).parent
        with open( str(x.absolute()) + '\\kan_reciept_kotu_template.hjson', 'r', encoding='utf-8') as f:
            return hjson.load(f)
    def getTemplateByPlace(self, place):
        '''template選択'''
        return self.template[place]
        