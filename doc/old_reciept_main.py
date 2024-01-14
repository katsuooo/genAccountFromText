
'''
以前のrecipt_main



'''

'''
reciept パーサ メイン
'''


from .deleter import deleter

deleter()

from .inputGroup import inputGroup
ig = inputGroup()
#ig.readAllInputs()      #self.allに全入力ファイルを読み込み, jsonにパース。
inputFileList = ig.readAllInputGroup()

#
# risona2はprj_statement_textでパースされるのでここでははじく
# dc系のデータも{}なのではじく
#
# kotuデータを作成しているが、placeListの作成に変更する。
# 次段で編集する
#
from .inputGroupSub.singleGroup import singleGroup
from .inputGroupSub.tojsonBuyAndPlaceList import tojsonBuyAndPlaceList
sg = singleGroup()
tbk = tojsonBuyAndPlaceList()

tbk.toJson(inputFileList['kaigi'])
tbk.toJson(inputFileList['shoumouhin'])
tbk.toJson(inputFileList['book'])
sg.toJson(inputFileList['single'])
#dg.toJson(inputFileList['dc'])
#rg.toJson(inputFileList['risona'])




import os
import shutil
#
# single_ryohi.jsonの移動
#
'''
spathx = ['prj_reciept','intermediate_json_reciept','single_ryohi.json']
sfname = os.path.sep.join(spathx)
print(os.path.exists(sfname))
ypathx = ['prj_reciept','output_json_place']
ydir = os.path.sep.join(ypathx)
if os.path.exists(ydir + os.path.sep + 'single_ryohi.json'):
    os.remove(ydir + os.path.sep + 'single_ryohi.json')
if os.path.exists(sfname):
    shutil.move(sfname, ydir)
'''
#
# place Listの編集
# 日ごとに集計する。
# 1日i交通費の生成としてみる。
#
# placeListでdailyの移動場所を整理後、kotu勘定を自動生成する。
# 手動交通データのミックスも検討する。
#
#
from .aggregatePlaceList import aggregatePlaceList
ap = aggregatePlaceList()
placeList = ap.readPlaceList()
daily = ap.aggregateDaily(placeList)
ap.saveDaily(daily)

#
# daily編集されたplace情報から交通費勘定生成用に場所を選択
# file化。保存。
#
selected = ap.selectPlace(daily)
ap.saveSelected(selected)






