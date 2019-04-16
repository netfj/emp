
def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()



# a = getmidstring(r'a:\bcd\efg','\\','\\')
# print(a)


path = 'c:\TEMP\tmp2\10.部门一'+'>'
# b = r'c:\TEMP\tmp2\10.部门一\20.科室2'+'>'
p0 = r'{}'.format(path)
print('p0:',p0)

p1 = path.replace('\\', '/').strip()
print(p1)
