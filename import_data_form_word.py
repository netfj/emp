#coding:utf-8
# @Info: 从人事档案表中提取数据
# @Author:Netfj@sina.com @File:import_data_form_word.py @Time:2019/3/30 6:50

import docx,logging
def logset():
    filename='runinfo.log'
    style='simplify'
    level_grade = logging.DEBUG
    LOG_FORMAT = "%(asctime)s|%(filename)s(%(lineno)d)%(funcName)s" \
                   "[%(levelname)s]%(message)s"
    DATE_FORMAT = "%m.%d.%H:%M"
    logging.basicConfig(filename=filename,
                        level=level_grade,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)
logset()

class pickup_emp():
    docx_file = ''
    data = {}
    tables_info = {}
    table_items = {}
    table_items_clean = {}
    db_table_0_a = {
        'name':'姓名', 'gender':'性别', 'birthday':'出生年月',
        'nation':'民族', 'native':'籍贯','birthplace':'出生地',
        'party_time':'入党时间', 'work_time':'参加工作时间','health':'健康状况',
        'profession':'专业技术职务','speciality':'熟悉专业有何专长',
        'education1':'全日制教育', 'academy1':'毕业院校系及专业',
        'education2':'在职教育', 'academy2':'毕业院校系及专业',
        'post_now':'现任职务',
        'post_will':'拟任职务',
        'post_remove':'拟免职务'
    }
    db_table_0_b = {
        'resume_time':'简历时间','resume_post':'简历岗位'
    }

    def __init__(self):
        pass

    # 更换文件
    def updata_word_file(self,docx_file):
        self.docx_file = docx_file
        doc = docx.Document(self.docx_file)
        self.tables = doc.tables  # 获取文件中的表格集
        self.tables_info.update(word文件名=self.docx_file)
        self.tables_info.update(表格数量=len(self.tables))
        for n in range(0,len(self.tables)):
            row = len(self.tables[n].rows)
            col = len(self.tables[n].columns)
            self.tables_info.update({'表格{}的行列数量（行，列）'.format(n):(row,col)})
        logging.info(self.tables_info)
        
    # 读取单元格的文本，参数：表序号、行号、列号
    def get_cell_text(self,table=0,row=0,col=0):
        t = self.tables[table].cell(row, col).text
        return t

    # 提取表的数据，保存在：self.table_items
    def import_data_from_word_file(self):
        for n in range(0,len(self.tables)):
            row = len(self.tables[n].rows)
            col = len(self.tables[n].columns)
            self.table_items[n]=[]
            for r in range(0,row):
                for c in range(0,col):
                    t = self.get_cell_text(table=n,row=r,col=c)
                    self.table_items[n].append(t)
        logging.info(self.table_items)

    def clean_data(self):
        # 清洗数据：1.将（简历之前）连续的重复的数据去除；
        #          2.简历之后数据不作处理；
        #          3.空数据删除, 换行符 '\n' 删除
        # 数据源：self.table_items[0]
        # 生成后保存的位置：self.table_items_clean.update['db_table_0_a']

        data = [i for i in self.table_items[0] if i != '']
        data = [i.replace(' ','').replace('　','').replace('\n','') for i in data]
        last = '?'
        del_items = []
        for n in range(0,len(data)):
            now = data[n]
            # print(n,'|',last,'|',now)
            if now == last:
                del_items.append(n)
            last = now
        print(del_items)
        data_clean = []
        for i in range(0,len(data)):
            if not i in del_items:
                data_clean.append(data[i])

        # 保存清理过的数据：表1的第1部分（简历之前）
        self.table_items_clean.update(db_table_0_a = data_clean)


    def import_to_db(self):



    def run(self):
        self.import_data_from_word_file()   # 导入数据
        self.clean_data()                   # 清洗数据
        self.

filelist = ['emp_sample.docx','emp_xxb.docx']
w = pickup_emp()
w.updata_word_file(filelist[1])
w.run()



import sys
sys.exit()
a = w.table_items
for i in a[0]:
    print(i)

for i in a[1]:
    print(i)