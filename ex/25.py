#coding:utf-8
# @Info:  建立部门、科室（中队）编码系统
# @Author:Netfj@sina.com @File:25.py @Time:2019/4/11 19:26
import os

class get_dir_list():
    def __init__(self, path = ''):
        self.path = path
        self.dir_list = []
        self.get_dir(self.path)

    def get_dir(self, path):
        if os.path.isdir(path):    # 如果是文件夹
            self.dir_list.append(path)
            list = os.listdir(path)
            for i in list:
                self.get_dir(os.path.join(path,i))

def get_bmks(file):
    path2 = os.path.dirname(file)
    path1 = os.path.dirname(path2)
    p2 = path1[path1.rfind('\\')+1:]
    p1 = path2[path2.rfind('\\')+1:]
    dm_bm = p1[0:2]
    dm_ks = dm_bm + p2[0:2]
    mc_bm = p1[p1.find('.')+1:p1.find('（')]
    mc_ks = p2[p2.find('.')+1:]
    return {'dm_bm':dm_bm,'mc_bm':mc_bm,'dm_ks':dm_ks,'mc_ks':mc_ks}

# p = get_dir_list(r'c:\temp\tmp2')
# print(p.dir_list)

a = get_bmks(r'c:\TEMP\tmp2\90.部门其它\10.AAA（10人）\test.txt')
print(a)