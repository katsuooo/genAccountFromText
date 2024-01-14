'''
勘定データ作成用小物
'''

from .fileio import fileio
from datetime import date

class kanUtil:
    def __init__(self, prj_dir):
        self.prj_dir = prj_dir
        pass
    def kanDateForm(self, pydate):
        '''datetime.date型のデータを8桁に変換'''
        return pydate.strftime('%Y%m%d')
    def convJpDate(self, orgDate):
        ''' xx月xx日をdatetimeに変換 '''
        fio = fileio(self.prj_dir)
        m = int(orgDate.split('月')[0])
        d = int(orgDate.split('月')[1].replace('日',''))
        y = int(fio.getYear())
        pydate = date(y,m,d)
        return self.kanDateForm(pydate)
    def convJpDateWithYear(self, orgDate):
        ''' xx年xx月xx日をdatetimeに変換 '''
        y = int(orgDate.split('年')[0])
        m = int(orgDate.split('年')[1].split('月')[0])
        d = int(orgDate.split('年')[1].split('月')[1].replace('日',''))
        pydate = date(y,m,d)
        return self.kanDateForm(pydate)
    def convSlashDate(self, orgDate):
        ''' yyyy/mm/ddをdatetimeに変換 '''
        fio = fileio(self.prj_dir)
        y = int(orgDate.split('/')[0])
        m = int(orgDate.split('/')[1])
        d = int(orgDate.split('/')[2])
        pydate = date(y,m,d)
        return self.kanDateForm(pydate)
    def convSlashOne(self, orgDate):
        ''' mm/ddをdatetimeに変換 '''
        fio = fileio(self.prj_dir)
        m = int(orgDate.split('/')[0])
        d = int(orgDate.split('/')[1])
        y = int(fio.getYear())
        pydate = date(y,m,d)
        return self.kanDateForm(pydate)
    def getStartDate(self):
        ''' yyyy0101 をもとめる '''
        fio = fileio(self.prj_dir)
        return fio.getYear() + '0101'
    def setKanDate(self, orgDate):
        '''kanjou仕様にdateを変換してself.kanにセット'''
        orgDate = orgDate.replace('"','').replace("'","")
        #orgDate = orgDate
        if '年' in orgDate:
            # xxxx年mm月xx日
            kanDate = self.convJpDateWithYear(orgDate)
        elif '月' in orgDate:
            kanDate = self.convJpDate(orgDate)
        elif orgDate.count('/') == 2:
            kanDate = self.convSlashDate(orgDate)
        elif orgDate.count('/') == 1:
            kanDate = self.convSlashOne(orgDate)
        elif len(orgDate) == 8:
            kanDate = orgDate
        return kanDate        
