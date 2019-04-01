#coding:utf-8
# @Info: 从人事档案表中提取数据
# @Author:Netfj@sina.com @File:word2table.py @Time:2019/3/30 6:50

import docx,logging
def logset():
    filename='runinfo.log'
    level_grade = logging.DEBUG
    LOG_FORMAT = "%(asctime)s|%(filename)s(%(lineno)d)%(funcName)s[%(levelname)s]%(message)s"
    DATE_FORMAT = "%m.%d.%H:%M"
    logging.basicConfig(filename=filename,
                        level=level_grade,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)
logset()

class pickup_emp():
    filelist = ['emp_sample.docx']
    db_table_0_a = {
        'name':'姓名', 'gender':'性别', 'birthday':'出生年月',
        'nation':'民族', 'native':'籍贯','birthplace':'出生地',
        'party_time':'入党时间', 'work_time':'参加工作时间','health':'健康状况',
        'profession':'专业技术职务','speciality':'熟悉专业有何专长',
        'education1':'全日制教育', 'academy1':'毕业院校系及专业',
        'education2':'在职教育', 'academy2':'毕业院校系及专业',
        'post_now':'现任职务',
        'post_will':'拟任职务',
        'post_remove':'拟免职务',
        'end':'简历'
    }
    db_table_0_b = {
        'resume_time':'简历时间','resume_post':'简历岗位'
    }

    def __init__(self,filelist=None):
        if filelist:
            self.filelist = filelist
            self.run()

    # 内部数据初始化
    def initialize(self):
        self.docx_file = ''             # 导入的 WORD 文件名：sample.docx
        self.tables_info = {}           # 提取的表的初始数据：原始信息
        self.table_info_clean = {}      # 清洗处理过后的数据：可用信息
        self.data2db = {}               # 将要导入到数据表中的数据：精准信息
        logging.debug('内部数据初始化')

    # 提取表的数据，保存在：self.table_items
    def import_data_from_word_file(self):
        items = []
        for n in range(0, len(self.tables)):
            row = len(self.tables[n].rows)
            col = len(self.tables[n].columns)
            for r in range(0, row):
                for c in range(0, col):
                    t = self.tables[n].cell(row, col).text

    # 更换文件
    def updata_word_file(self, docx_file):
        print(docx_file)
        self.initialize()  # 将内部数据初始化
        self.docx_file = docx_file  # 更换文件名
        doc = docx.Document(self.docx_file)  # 打开文件
        self.tables = doc.tables  # 获取文件中的表格集

        # 收集有关信息, 保存在：self.tables_info['tables_info']
        tb_info = {'文件名':self.docx_file}                   # 文件名
        tb_info.update({'表格数量':str(len(self.tables))})  # 表格数量
        for n in range(0,len(self.tables)):
            row = len(self.tables[n].rows)
            col = len(self.tables[n].columns)
            tb_info.update({'表格{}的行列数量（行，列）'.format(n):(row,col)})
        self.tables_info.update(tables_info = tb_info)

    # 提取表的数据，保存在：self.tables_info['items_text']
    def extract_from_word(self):
        for n in range(0, len(self.tables)):
            row = len(self.tables[n].rows)
            col = len(self.tables[n].columns)
            self.table_items[n] = []
            for r in range(0, row):
                for c in range(0, col):
                    t = self.get_cell_text(table=n, row=r, col=c)
                    self.table_items[n].append(t)
        logging.info(self.table_items)

    def run(self):
        logging.info('文件列表:'+  ('|').join(self.filelist))
        for f in self.filelist:
            self.updata_word_file(f)
            logging.debug(self.tables_info)

filelist = ['emp_sample.docx','emp_xxb.docx']
filelist = [ filelist[0] ]
w = pickup_emp(filelist)

import sys
sys.exit()
