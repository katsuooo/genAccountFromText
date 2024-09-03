'''
kan_template.json interface
>>> change json to hjson
'''
import json
import hjson
import pathlib

class templater:
    def __init__(self,tempHjson):
        #self.template = self.readTemplate()
        self.template = tempHjson

    def readTemplate(self):
        '''templete.jsonを読み込み'''
        #x = pathlib.Path(__file__).parent
        #with open( str(x.absolute()) + '\kan_reciept_template.hjson', 'r', encoding='utf-8') as f:
        #with open( '../choData/kan_reciept_template.hjson', 'r', encoding='utf-8') as f:
        #    return hjson.load(f)
        pass

    def getTemplateByFname(self, fname):
        '''template選択'''
        key_label = fname.split('_')
        if key_label[0] == 'single':
            if key_label[1] == 'yachin':
                if len(key_label) > 2:
                    sub_key = key_label[2]
                else:
                    sub_key = key_label[1]
                if sub_key == 'm':
                    return self.template['yachin']['m']
                elif sub_key == 'y':
                    return self.template['yachin']['y']
                elif sub_key == 'oh':
                    return self.template['yachin']['oh']
                elif sub_key == 'om':
                    return self.template['yachin']['om']
                else:
                    return self.template['yachin']['monthly']
            #''' zappiのコマンド解析をファイル名に変更'''
            #'''            
            #elif key_label[1] == 'zappi':
            #    if key_label[2] == 'u':
            #        return  self.template['single']['zappi_u']
            #    else:
            #        return self.template['single']['zappi']
            #'''
            elif key_label[1] == 'zappi':       
                if len(key_label) >= 3:
                    if key_label[2] == 'u':
                        return  self.template['single']['zappi_u']
                    elif key_label[2] == 'r':
                        return  self.template['single']['zappi_r']
                    elif key_label[2] == 'm':
                        return  self.template['single']['zappi_m']
                    else:
                        return self.template['single']['zappi']    
                else:
                    return self.template['single']['zappi']
            elif key_label[1] == 'tax':
                #支払い分のみかく。発生分もどこかにかく。
                return self.template['single']['tax_shouhi_zei_shiharai']    
                '''    
                #消費税は２クエリを生成
                #sub-keyをアペンドしておく
                print(key_label)
                if key_label[2] == 'h':
                    #発生
                    return self.template['single']['tax_shouhi_zei_hassei']    
                elif key_label[2] == 's':
                    #支払
                    return self.template['single']['tax_shouhi_zei_shiharai']   
                raise KeyError("tax sub-key error, h or s", key_label[2]) '''
            else:
                return self.template['single'][key_label[1]]
                
        else:
            return self.template[key_label[0]]
        