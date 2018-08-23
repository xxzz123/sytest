#coding:utf-8

class jiekou():

    def CSH(self):
        url = 'http://210.22.89.58:37278/afterloanapi/'
        header = {'Content-Type': 'application/json'}
        return url, header


# ss = jiekou()
# print(ss.CSH()[0])