#
#
# レシートテキストのパース
#
#
#
#


print('-'*20+'\n'+'start reciept-main\n'+'-'*20+'\n')

#
# 既存のファイルの消去
#
from .pre_process.deleter import deleter

deleter()

#
# 前準備 
#
# 前回パースデータの削除
# テキストファイル全ファイルの読み込み
#
from .pre_process.readAllFile import inputGroup
ip = inputGroup()
allFile = ip.readAllInputGroup()
#print(allFile)

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
from .pre_process.inputGroupSub.singleGroup import singleGroup
from .pre_process.inputGroupSub.tojsonBuyAndPlaceList import tojsonBuyAndPlaceList
sg = singleGroup()
tbk = tojsonBuyAndPlaceList()

tbk.toJson(allFile['kaigi'])
tbk.toJson(allFile['shoumouhin'])
tbk.toJson(allFile['book'])
#tbk.toJson(allFile['tushin'])
sg.toJson(allFile['single'])
#
# 会議費
#

#
# 交際費
#

#
# 交通費作成   // 交通費はpitapaデータをつかう個々の勘定からの交通費作成はやめる
#
'''
from .aggregatePlaceList import aggregatePlaceList
ap = aggregatePlaceList()
placeList = ap.readPlaceList()
daily = ap.aggregateDaily(placeList)
ap.saveDaily(daily)
'''




'''レシートテキスト２ndパース'''
#print('|'*10 + ' reciept-2nd parse- ' + '|'*10)
'''
print_title(' reciept-2nd parse- ')
from prj_reciept_kan_templater import reciept_kan_templater_main
reciept_kan_templater_main
'''




