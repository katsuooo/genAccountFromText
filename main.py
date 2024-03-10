#
# gen account from text
#
# テキスト化されたデータの集計
# 移動を含むデータの交通費の生成
# 生成した勘定データをmongodbにロード
#
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
from pre_parse_reciept import pre_reciept_main

#pre_reciept_main


#
# ラフパースから勘定に
#
from parse_reciept import reciept_kan_templater_main

#reciept_kan_templater_main


