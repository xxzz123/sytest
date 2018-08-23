#coding:utf-8

import os,json
# cur_path = os.path.dirname(os.path.realpath(__file__))

cur_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
path2 = cur_path + r'\file'
print(cur_path)
datas = []

print (os.path.exists(path2+ r'\jinjianRes.txt'))
# with open(path2 + r'\jinjian.txt',  'rb+') as f:
#     uu = str(f.readlines())
#     print(uu)
#     print('=='*80)
#     line = uu.replace("b'", "")
#     line = line.replace(r"\r\n',", "")
#     line = line.rstrip(" ")
#     print(line)
#     print('**'*80)
#     print (type(line))
#     print (type(eval(json.dumps(line))))
    # j1_son = json.dumps(line)
    # print(j1_son)
    # print('%%'*80)
    # print (j1_son[24])
