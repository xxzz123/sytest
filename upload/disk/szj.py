#coding:utf-8

from bs4 import  BeautifulSoup
import requests
import  urllib,urllib2
import os,re


key = raw_input(u"请输入你要搜索的关键词：")
print key
# word=%E5%AE%8B%E4%BB%B2%E5%9F%BA&
url= r'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=utf-8&word='+key+'&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'

# url= r'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+key+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E5%AE%8B%E4%BB%B2%E5%9F%BA&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&cg=star&pn=60&rn=30&gsm=3c&1505470672332='
response = urllib2.urlopen(url)
#文本格式输出
content = requests.get(url).text
#筛选出objURL  图片下载链接的地址
ic_url = re.findall('"objURL":"(.*?)",',content,re.S)
# print ic_url
i = 0
print  "长度：", ic_url.__len__()
for each in ic_url:
    print each
    try:
        pic = requests.get(each, timeout=10)
    except Exception,e :
        print '【错误！】当前图片无法下载！'
        continue
    string = 'husband\\' + str(i) + '.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1



