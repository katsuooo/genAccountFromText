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
    def __init__(self):
        self.clearFiles()
    def filesDelete(self, folder):
        '''folder list内のファイルを削除'''

        for root, dirs, files in os.walk(os.path.sep.join(folder)):
            for f in files:
                fname = os.path.sep.join(folder) + os.path.sep + f
                os.remove(fname)

    def clearFiles(self):
        '''過去に生成されたファイルを消す'''
        folders1 = ['prj_reciept','intermediate_json_kotu']
        folders2 = ['prj_reciept','intermediate_json_reciept']
        folders3 = ['prj_reciept','out_json_statement']
        '''
        for folder in folders1:
            self.filesDelete(folder)
        for folder in folders2:
            self.filesDelete(folder)
        for folder in folders3:
            self.filesDelete(folder)
        '''
        self.filesDelete(folders1)
        self.filesDelete(folders2)
        self.filesDelete(folders3)