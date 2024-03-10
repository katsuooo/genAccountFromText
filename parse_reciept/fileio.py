''' file io '''


import os
import json
import pathlib

class fileio:
    def __init__(self, prj_dir):
        self.prj_dir = prj_dir
        pass
    def getFileNamesFromFolderExdir(self, dirName):
        '''ディレクトリ内のファイル名リストを返す'''
        '''指定ディレクトリのファイルのみ'''
        labels = []
        for root, dirs, files in os.walk(dirName):  
            if root == dirName:
                for f in files:
                    labels.append(f.split('.')[0])
        return labels
    def readJson(self, pathx, label):
        fname = os.path.sep.join([pathx, label])
        if '.json' not in fname:
            fname += '.json'
        with open(fname, 'r', encoding='utf-8') as f:
            return json.load(f)
    def getParent(self):
        return str(pathlib.Path(__file__).parents[1])
    def readAll(self, pre_file_dir):
        '''jsonStatementをjson化'''
        ''' --->  intermediate_json_statement をjson化'''
        ''' prj_statement_text/intermediate_json/risona_risona2.jsonも追加u'''
        dirName = os.path.sep.join([self.getParent(), pre_file_dir,'intermediate_json_reciept'])
        labels = self.getFileNamesFromFolderExdir(dirName)
        all = {}
        for label in labels:
            all[label] = self.readJson(dirName, label)
        return all
    def readKotuAll(self):
        '''prj_project/intermediate_json_kotuフォルダを全リードして返す'''
        dirName = os.path.sep.join([self.getParent(), 'pre_parse_reciept','intermediate_json_kotu'])
        labels = self.getFileNamesFromFolderExdir(dirName)
        all = {}
        for label in labels:
            all[label] = self.readJson(dirName, label)
        return all
    def getYear(self):
        fname = os.path.sep.join(['config_json', 'choConfig.json'])
        with open(fname, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config['year']
    def writeJson(self, jd, label):
        '''out_jsonフォルダに保存'''
        fname = os.path.sep.join([str(pathlib.Path(__file__).parents[0]), 'out_json', label])
        if '.json' not in fname:
            fname += '.json'
        if not os.path.isdir('parse_reciept/out_json'):
            os.mkdir('parse_reciept/out_json')
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(jd, f, ensure_ascii=False, sort_keys=False, indent=2)
    def saveKan(self, jd, name):
        self.writeJson(jd, name)
    def saveKotuKan(self, jd, name):
        '''out_json_kotuフォルダに保存'''
        fname = os.path.sep.join([str(pathlib.Path(__file__).parents[0]), 'out_json_kotu', name])
        if '.json' not in fname:
            fname += '.json'
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(jd, f, ensure_ascii=False, sort_keys=False, indent=2)
    def appendKan(self, jd, name):
        fname = os.path.sep.join([str(pathlib.Path(__file__).parents[0]), 'out_json', name])
        if '.json' not in fname:
            fname += '.json'
        with open(fname, 'r', encoding='utf-8') as f:
            rd = json.load(f)
        for j in jd:
            rd.append(j)
        self.saveKan(rd, name)
    def readConfig(self, configName):
        '''config file read'''
        #fpath = ['config_json', configName + 'Config']
        return self.readJson('config_json', configName + 'Config')
    def getFormBase(self):
        '''kan form baseをよむ'''
        config = self.readConfig('cho')
        return config['FORM_BASE']
    def getParent(self):
        return str(pathlib.Path(__file__).parents[1])