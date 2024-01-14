'''text arangement'''

class textUtil:
    def __init__(self):
        pass
    def textShaping(self, text):
        '''text shaping
        delete '#' included line
        delete \n
        to list line by line
        '''
        lines = text.split('\n')
        news = []
        for l in lines:
            if '#' in l:
                continue
            elif l == '':
                continue
            elif len(l.replace(' ','')) == 0:
                continue
            l = l.replace('\n', '')
            l = l.replace('　', ' ')
            news.append(l)
        return news