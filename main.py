#
# gen account from text
#
# テキスト化されたデータの集計
# 移動を含むデータの交通費の生成
# 生成した勘定データをmongodbにロード >>> dbつかわず、jsonで処理
#
# データフォルダをchoDataに変更
#

#
# fileのioをここに書いて見通しをよくする
#

#
# レシートテキストから勘定を生成
#
#
# deleater >>> pre_parse_reciept/pre_reciept_mainで実行
# pre_parse_reciept/pre_process/intermediate_json_reciept
#





#
# 事前ラフパース
#
#from pre_parse_reciept import pre_reciept_main
#pre_reciept_main







print('-'*20+'\n'+'start reciept-main\n'+'-'*20+'\n')


import json
#年度の取得
year = ""
with open('../choData/config.json','r',encoding='utf-8') as f:
    config = json.load(f)
    year = config['year']

basePath = '../choData/' + year + '/'
print(basePath)

#
# 既存のファイルの消去
#
from pre_process.deleter import deleter

deleter([basePath + 'text_intermediate/'])
#
# 前準備 
#
# 前回パースデータの削除
# テキストファイル全ファイルの読み込み
#
from pre_process.readAllFile import inputGroup
ip = inputGroup()
allFile = ip.readAllInputGroup(basePath + 'text_input/')

def save_intermediate(d, fn):
    if '.json' not in fn:
        fn += '.json'
    with open(fn,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=4)

def save_output(d, fn):
    if '.json' not in fn:
        fn += '.json'
    with open(fn,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=4)

def save_exclude(d, fn):
    if '.json' not in fn:
        fn += '.json'
    with open(fn,'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False,indent=4)

input_config = {}

with open(basePath + 'text_config/inputsConfig.json','r',encoding='utf-8') as f:
    input_config = json.load(f)

#
# テキストファイルをjsonに変換(粗変換)
#
#
# risona2はprj_statement_textでパースされるのでここでははじく
# dc系のデータも{}なのではじく
#
# kotuデータを作成しているが、placeListの作成に変更する。
# 次段で編集する
#
        
from pre_process.inputGroupSub.singleGroup import singleGroup
from pre_process.inputGroupSub.tojsonBuyAndPlaceList import tojsonBuyAndPlaceList
sg = singleGroup(input_config)
tbk = tojsonBuyAndPlaceList()

[save_intermediate(jd, basePath + 'text_intermediate/' + jd[0]['fname']) for jd in tbk.getJsonList(allFile['kaigi'], input_config)]
[save_intermediate(jd, basePath + 'text_intermediate/' + jd[0]['fname']) for jd in tbk.getJsonList(allFile['shoumouhin'], input_config)]
[save_intermediate(jd, basePath + 'text_intermediate/' + jd[0]['fname']) for jd in tbk.getJsonList(allFile['book'], input_config)]
#tbk.getJsonList(allFile['shoumouhin'], basePath + 'text_intermediate/')
#tbk.getJsonList(allFile['book'], basePath + 'text_intermediate/')
#tbk.toJson(allFile['tushin'])
#sg.toJson(allFile['single'], basePath + 'text_intermediate/')
[save_intermediate(jd, basePath + 'text_intermediate/' + jd[0]['fname']) for jd in tbk.getJsonList(allFile['single'], input_config)]

#帳簿外のデータ
[save_exclude(jd, basePath + 'text_exclude/' + jd[0]['fname']) for jd in tbk.getJsonList(allFile['exclude'], input_config)]





#
# ラフパースから勘定に
#
from parse_reciept import reciept_kan_templater_main

#reciept_kan_templater_main

rkt = reciept_kan_templater_main.recieptParser()
rkt.fileClear(basePath + 'text_output/')
intermediateAll = rkt.readAllIntermediate(basePath + 'text_intermediate/')



import hjson
tempHjson = []
#with open(basePath + 'text_config/kan_reciept_template.hjson','r',encoding='utf-8') as f:
'''
year = ''
with open('../choData/config.json','r',encoding='utf-8') as f:
    j = json.load(f)
    year = j['year']
'''
with open(basePath + 'text_config/kan_reciept_template.hjson','r',encoding='utf-8') as f:
    tempHjson = hjson.load(f)

from parse_reciept import templater
templateFunc = templater.templater(tempHjson)    #templateのセレクタ関数

from parse_reciept import parseRecieptKanFromTemplate
prk = parseRecieptKanFromTemplate.parseRecieptKan(templateFunc)

[save_output(prk.parsePerFile(jKey, intermediateAll[jKey], year, templateFunc.getTemplateByFname(jKey)), basePath + 'text_output/' + jKey) for jKey in intermediateAll]

#[save_exclude(prk.parsePerFile(jKey, intermediateAll[jKey], year, templateFunc.getTemplateByFname(jKey)), basePath + 'text_exclude/' + jKey) for jKey in intermediateAll]




