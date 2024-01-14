''' file delete '''

import os
class deleter:
    def __init__(self, prj_dir):
        print('delete-templater-files', prj_dir)
        self.clearFiles()
    def filesDelete(self, folder):
        '''folder list内のファイルを削除'''
        for root, dirs, files in os.walk(folder):
            for f in files:
                os.remove(os.path.sep.join([folder, f]))

    def clearFiles(self):
        '''過去に生成されたファイルを消す'''
        ''' cleaned directorys
        '''
        folders1 = ['parse_reciept/out_json']
        for folder in folders1:
            self.filesDelete(folder)
        folders2 = ['parse_reciept/out_json_kotu']
        for folder in folders2:
            self.filesDelete(folder)
