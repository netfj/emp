#coding:utf-8
# @Info:   
# @Author: Netfj@sina.com @File:10.py @Time:2019/4/4 9:19

# s=r'v:\User\人员档案资料\01.机关\01.办公室（11人）'
# print(s)
#
# import os
# e = os.path.splitext(r'c:\Users\Fj\py\emp.abc\abc.xyz.ypo')
# print(e[1])


a = {1:[1,2],2:[234]}
print(len(a))

print(a.get(0))

it = a.values()
print(it)

print([1,2] in it)
print([234] in it)
print([] in it )

list0 = [1,2,9,9,3,2,3,4,5,6,8]
lis = []
[lis.append(i) for i in list0 if not i in lis]
print(lis)