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
        folders1 = ['pre_parse_reciept','pre_process','intermediate_json_reciept']
        folders2 = ['parse_reciept','out_json']
        #folders3 = ['prj_reciept','out_json_statement']
        self.filesDelete(folders1)
        self.filesDelete(folders2)
        #self.filesDelete(folders3)