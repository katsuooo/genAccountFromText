''' yachin input '''
'''
交通費なし
地代家賃 - 事業主借
'''
# m/d xxxx の後にいれる
# y 年初遅れ入金。前月末の未払い処理しない。
# o は遅れ入金日。前月末に未払いで処理する。未払いデータは記載しない。
# m は未払い日(年度末時)
# h 火災保険で金額付き

'''
ここで勘定を用意しないので、どういう形にしようか。
特殊な形に一度変換して、jsonInputsParseで勘定に変換？
なんだそれ的ではありますが、勘定値をコンフィグからとるところで、ファイルタイプに加えて
キーワードを用意するか、ファイルを変えてしまえばいいのか。
none >>> 月末家賃支払い
y >>> 1クエリ 前年未払い埋め
o >>> 前月末の未払い、支払い時の未払い処理の２クエリを生成 >>> 2fileになるかな？
m >>> 普段の未払いは書かないが、年末は払いのクエリが翌年になるので書く。１クエリ
h >>> 保険。１クエリだね。勘定なんだ？ hの後に金額をかく。後にですよ！！

普段の未払いはどうなってるの？？
省略しちゃってるのか。>>> oがそれじゃん。
'''
'''
json配列で保存
output file名 >>> jsonInputs
yachin
yachin_y 事業主借 - 未払金　前年未払い埋め
yachin_om(遅れ時未払い勘定)　地代家賃 - 未払金
yachin_oh(遅れ時支払い勘定)  事業主借 - 未払金
yachin_m 年度末の見払い １クエリ 地代家賃 - 未払金     
yachin_h　地代家賃 - 事業主借　memo= 保険等
'''

from .fileIo import fileIo
from .inputsUtil import inputsUtil

class singleYachin:
    def __init__(self, fname, jd):
        '''jd = [line1, line2, ...]'''
        self.yachin = []
        self.yachin_y = []
        self.yachin_om = []
        self.yachin_oh = []
        self.yachin_m = []
        self.yachin_h = []
        self.toJson(fname, jd)
    def fetchCommand(self, items):
        date = items[0]
        command = items[1]
        memo = ''
        iu = inputsUtil()
        print(items)
        '''yomh コマンド解析'''
        if command == 'y':
            val = iu.getYachin()
            memo = '前年未払い埋め'
            jd = iu.parseBuy(date,val,memo)
            self.yachin_y.append(jd)
        elif command == 'o':
            val = iu.getYachin()
            memo = '月末払い忘れ'
            zengetu_matsu = iu.getLaseMonthsMatsubi(date)
            jd = iu.parseBuy(zengetu_matsu,val,memo)
            self.yachin_om.append(jd)
            memo = '未払い埋め'
            jd = iu.parseBuy(date,val,memo)
            self.yachin_oh.append(jd)
        elif command == 'm':
            val = iu.getYachin()
            memo = '年度末払い忘れ'
            jd = iu.parseBuy(date,val,memo)
            self.yachin_m.append(jd)
        elif command == 'h':
            memo = '保険等'
            val = iu.getYachin()
            jd = iu.parseBuy(date,val,memo)            
            self.yachin_h.append(jd)
    def normalPay(self, date):
        '''にこにこ月末払い'''
        memo = ''
        iu = inputsUtil()
        val = iu.getYachin()
        jd = iu.parseBuy(date,val,memo)
        self.yachin.append(jd)
    def decoding(self, line):
        ''' line中のコマンド有無、デコードを行う'''
        items = line.split(' ')
        if len(items) > 1:
            self.fetchCommand(items)
        else:
            self.normalPay(items[0])
    def saveJson(self, newd, fname):
        fio = fileIo()
        fio.saveInputs(newd, fname)
    def saveYachins(self, fname):
        '''yachin 5fileの保存'''
        print('yachin-',fname,self.yachin)
        if len(self.yachin) != 0:
            self.saveJson(self.yachin, fname)
        if len(self.yachin_y) != 0:
            yname = fname + '_y'        
            self.saveJson(self.yachin_y, yname)
        if len(self.yachin_om) != 0:
            yname = fname + '_om'
            self.saveJson(self.yachin_om, yname)
        if len(self.yachin_oh) != 0:
            yname = fname + '_oh'
            self.saveJson(self.yachin_oh, yname)
        if len(self.yachin_m) != 0:
            yname = fname + '_m'
            self.saveJson(self.yachin_m, yname)
        if len(self.yachin_h) != 0:
            yname = fname + '_h'
            self.saveJson(self.yachin_h, yname)
    def parse(self, fname, lines):
        '''text linesのパース'''
        '''lines [m/d, xxxx(val) only or plus command charctor]'''
        for line in lines:
            self.decoding(line)
        self.saveYachins(fname)
    def toJson(self, fname, yachinJson):
        '''text >>> json'''
        self.parse(fname, yachinJson)
