'''
全テキストの読み込み
'''
'''
format
input textをすべてリードしjson化
inputs = 
{
    input
},
'''


from .inputGroupSub.fileIo import fileIo
from .inputGroupSub.singleGroup import singleGroup
from .inputGroupSub.tojsonBuyAndKotu import tojsonBuyAndKotu




class AutoTree(dict):
    """Dictionary with unlimited levels"""
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

class inputGroup:
    def __init__(self):
        self.inputs = {}
        self.fio = fileIo()

    def genCategorys(self, fnames):
        '''filenameの先頭名のリストをつくる
        重複ははぶく
        '_'を含まないfnameははぶく
        '''
        all = []
        for f in fnames:
            if '_' not in f:
                continue
            pre = f.split('_')[0]
            all.append(pre)
        noDupricate = []
        for x in all:
            if x not in noDupricate:
                noDupricate.append(x)
        return noDupricate

    def conCatarogAndFname(self, catList, fnames):
        '''catalogにfileNamesをつけてjsonにする'''
        jd = {}
        for c in catList:
            cList = []
            for f in fnames:
                if c in f:
                    cList.append(f)
            jd[c] = cList
        return jd

    def getInputGroupAllList(self):
        '''input groupのリストを作成する
        textInputsフォルダのファイル名リストからグループリストを作成
        '''
        fileNames = self.fio.getFileNamesFromFolder('reciept_text')
        catList = self.genCategorys(fileNames)
        return self.conCatarogAndFname(catList, fileNames)

    def getInputGroupList(self, category):
        '''input groupの指定カテゴリのリストを返す'''
        return self.igList[category]

    def toJson(self, all):
        '''textデータをjsonフォームに加工
        group毎にformが違ったりする。
        '''
        rg = risonaGroup()
        dg = dcGroup()
        sg = singleGroup()
        tbk = tojsonBuyAndKotu()
        tbk.toJson(all['kaigi'])
        tbk.toJson(all['shoumouhin'])
        tbk.toJson(all['book'])
        print('all-single',all['single'])
        sg.toJson(all['single'])
        dg.toJson(all['dc'])
        rg.toJson(all['risona'])
        return all

    def readAllInputs(self):
        '''igListから全ファイルを読み込み、dictにする
        {
            group_name: {filename: text(shaped)} 
        }
        rough jsonへのパースも行う
        '''
        igList = self.getInputGroupAllList()
        all = AutoTree()    #def above
        #全ファイルを読み整形しjson化
        for gname in igList:
            for fname in igList[gname]:
                all[gname][fname] = self.fio.readInputText(fname)
        alljson = self.toJson(all)
        self.inputs = alljson

    def getInputGroup(self, group):
        return self.inputs[group]
    
    def readAllInputGroup(self):
        '''
        input text を読み込み、group単位でまとめたdictにして返す
        '''
        igList = self.getInputGroupAllList()
        all = AutoTree()    #def above
        #全ファイルを読み整形しjson化
        for gname in igList:
            for fname in igList[gname]:
                all[gname][fname] = self.fio.readInputText(fname)
        return all
    
