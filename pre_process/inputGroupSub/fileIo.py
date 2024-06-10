''' file ios '''

import json
import os
from .textUtil import textUtil
import pathlib

class fileIo:
    def __init__(self):
        self.tu = textUtil()
    def readJson(self, fpath):
        '''json read
           fpath: file path list
        '''
        fname = os.path.sep.join(fpath)
        if '.json' not in fname:
            fname += '.json'
        with open(fname, 'r', encoding='utf-8') as f:
            jd = json.load(f)
        return jd
    def checkDirUmu(self, directory_path):
        if os.path.exists(directory_path):
            #print(f'{directory_path} は存在します。')
            if os.path.isdir(directory_path):
                #print(f'{directory_path} はディレクトリです。')
                return
            else:
                #print(f'{directory_path} はディレクトリではありません。')
                pass
        else:
            #print(f'{directory_path} は存在しません。')
            pass
        os.makedirs(directory_path)

    def writeJson(self, jd, fpath):
        '''json write
        fpath: file path list
        '''
        dir_path = fpath[0:len(fpath)-1]
        self.checkDirUmu(os.path.sep.join(dir_path))
        fname = os.path.sep.join(fpath)
        if '.json' not in fname:
            fname += '.json'
        with open(fname, 'w', encoding='utf-8') as f:
            jd = json.dump(jd, f, ensure_ascii=False, indent=2, sort_keys=False)
    def readText(self, fpath):
        '''text file read
        '''
        fname = os.path.sep.join(fpath)
        if '.txt' not in fname:
            fname += '.txt'
        with open(fname, 'r', encoding='utf-8') as f:
            text = f.read()
        shaped = self.tu.textShaping(text)
        return shaped

    def getFileNamesFromFolder(self, dirName):
        '''ディレクトリ内のファイル名リストを返す'''
        '''dirパスに年度を追加する'''
        year = self.getConfigYear()
        xpath = [year, dirName]
        dirPath = os.path.sep.join(xpath)
        labels = []
        for root, dirs, files in os.walk(dirPath):  
            for f in files:
                labels.append(f.split('.')[0])
        return labels

    def getFileNameFromPath(self, input_path):
        '''pathにあるファイル名リストを返す サブディレクトリを除外する'''
        labels = []
        file_list = []
        for root, dirs, files in os.walk(input_path):
            for f in files:
                item_path = os.path.join(input_path, f)
                if os.path.isfile(item_path):
                    labels.append(f.split('.')[0])
        return labels
    
    def list_files_without_subdirectories(self, directory):
        #ディレクトリのファイルリストを返す　サブディレクトリを含まない
        file_list = []
        labels = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                file_list.append(item_path)
        for f in file_list:
            labels.append(f.split('.')[0])
        return labels
        
    def readInputText(self, fname):
        '''textInputsからtxtを読む'''
        print(fname)
        if '.txt' not in fname:
            fname += '.txt'
        with open(fname, 'r', encoding='utf-8') as f:
            text = f.read()
        shaped = self.tu.textShaping(text)   
        return shaped
    
    def getParent(self):
        return str(pathlib.Path(__file__).parents[1])
    
    def saveIntermediateKotu(self, jd, label):
        #kotu中間ファイル保存
        fpath = [self.getParent(), 'intermediate_json_kotu', label + '.json']
        self.writeJson(jd, fpath)
    def getIntermediateKotu(self, fname):
        fpath = [self.getParent(), 'intermediate_json_kotu', fname + '.json']
        return self.readJson(fpath)
    def getIntermediateKotuDaykey(self, fname):
        fpath = [self.getParent(), 'intermediate_json_kotuDaykey', fname + '.json']
        return self.readJson(fpath)
    
    def saveInputsKotu(self, jd, fname):
        fpath = [self.getParent(), 'intermediate_json_kotu', fname + '.json']
        self.writeJson(jd, fpath)

    def saveInputs(self, jd, fname):
        '''text to jsonの初期返還ファイルの保存
        '''
        fpath = [self.getParent(), 'intermediate_json_reciept', fname + '.json']
        self.writeJson(jd, fpath)

    def saveReciept(self, jd, fname):
        fpath = [self.getParent(), 'out_json_statement', fname + '.json']
        self.writeJson(jd, fpath)
        
    def getConfig(self, name):
        '''name+'Config'.jsonをかえす'''
        fpath = ['config_json', name + 'Config']
        return self.readJson(fpath)    
    
    def getConfigYear(self):
        '''config_json/choConfigのyearを取得する'''
        config = self.getConfig('cho')
        return config['year']
    
    def savePlaceInfo(self, jd, fname):
        '''place-infoを保存する'''
        fpath = [self.getParent(), 'intermediate_json_placeInfo', fname + '.json']
        self.writeJson(jd, fpath)
    def getStationList(self):
        config = self.getConfig('kotu')
        return config["public_transport_costs"].keys()