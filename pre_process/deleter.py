''' file delete '''
'''
中間ファイル群を消去
prj_reciept/ intermediate_json_kotu
           / intermediate_json_reciept
           / out_json_statement
フォルダ内の全ファイル
'''

import os
import copy
class deleter:
    def __init__(self, pathList):
        self.clearFiles(pathList)

    def filesDelete(self, folder):
        '''folder list内のファイルを削除'''
        for root, dirs, files in os.walk(os.path.sep.join(folder)):
            for f in files:
                fname = os.path.sep.join(folder) + os.path.sep + f
                os.remove(fname)

    def fileDeleteInPath(self, delPath):
        for f in os.listdir(delPath):
            if not os.path.isdir(delPath + f):
                os.remove(delPath + f)

    def clearFiles(self, pathList):
        '''過去に生成されたファイルを消す'''
        for p in pathList:
            self.fileDeleteInPath(p)
