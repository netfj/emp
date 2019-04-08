#coding:utf-8
# word DOC 文件格式，转换成为 docx 文件格式

from win32com import client
from os import path,makedirs
from tempfile import gettempdir
from random import randint
from shutil import rmtree
from time import sleep

def doc2docx(doc_name=None,docx_name=None):
    if not doc_name:
        msg = '没有传递文件！'
        print(msg)
        return False

    doc_name = path.realpath(doc_name)

    if not path.exists(doc_name):
        msg = doc_name + ' 文件不存在!'
        print(msg)
        return False

    # 临时目录：操作系统的临时目录 + 本系统特定的目录
    sys_tmp = path.join(gettempdir(), '_doc2docx')
    if not path.exists(sys_tmp):  # 临时目录：如果没有，则创建
        makedirs(sys_tmp)

    # 单个进程的目录，这样大批量处理时，会提高速度
    tmp_path = path.join(sys_tmp, str(randint(0, 9999999)))
    if not path.exists(tmp_path):
        makedirs(tmp_path)

    # 临时目录：操作系统的临时目录 + 本系统特定的目录
    sys_tmp = path.join(gettempdir(), '_doc2docx')
    if not path.exists(sys_tmp):  # 临时目录：如果没有，则创建
        makedirs(sys_tmp)

    # 单个进程的目录，这样大批量处理时，会提高速度
    tmp_path = path.join(sys_tmp, str(randint(0, 9999999)))
    if not path.exists(tmp_path):
        makedirs(tmp_path)

    if not docx_name:
        docx_name = path.join(tmp_path,path.basename(doc_name)+'.docx')

    try:    # doc ==> docx
        word = client.Dispatch("Word.Application")
        doc  = word.Documents.Open(doc_name)
        doc.SaveAs(docx_name,16)
        doc.Close()
        word.Quit()
    except Exception as e:
        msg = '转换失败：{}'.format(e)
        print(msg)
        return False
    else:
        print('转换成功:',docx_name)
        return docx_name

def clean_tmp_path():
    # 清理文件: 如果转换扫文件很多，要处理完成后清理
    # 临时目录：操作系统的临时目录 + 本系统特定的目录
    sys_tmp = path.join(gettempdir(), '_doc2docx')
    n = 1
    while True:
        try:
            rmtree(sys_tmp)
            msg = '清理操作成功！'
            print(msg)
            return True
            break
        except Exception as e:
            msg = '清理操作失败:{}'.format(e)
            sleep(1)
            if n > 10: break  # 偿试 n 次
            print(msg)
            return False
        n += 1

doc2docx(doc_name='emp_sample_word2003.doc')
# clean_tmp_path()

