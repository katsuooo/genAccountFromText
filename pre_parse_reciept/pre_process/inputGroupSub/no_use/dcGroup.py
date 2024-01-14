''' dc text >>> json '''
'''
(dc引き落とし経費)
電気
ガス
携帯
ネット
'''
'''
tojson.textのデータ
keitaiのみ
他はcsvから読み込む
'''
from .singleParseNoKotu import singleParseNoKotu

class dcGroup:
    def __init__(self):
        pass
    def parseCsv(self):
        '''dc, denki, gusのデータをinfoRecieptからよむ'''
        pass
    def toJson(self, dcs):
        '''dcsはkeitaiのみ'''
        for fname in dcs:
            singleParseNoKotu(fname, dcs[fname])  
        self.parseCsv() 
