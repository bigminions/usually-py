# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from xlrd import Book

import os

# 说明:
# 读取简单的excel表中的内容

# 打开excel文件
def open_excel(filename):
    if not filename:
        return None
    try:
        data = xlrd.open_workbook(filename)
        return data
    except Exception:
        print("Exception when open file {}".format(filename))

# 处理每一行
def handle_row(filename, row):
    rowData = {}
    rowData['one'] = row[1]
    rowData['two'] = row[2]
    rowData['three'] = row[3]
    rowData['four'] = row[4]
    # 处理时间
    rowData['five'] = datetime(*xldate_as_tuple(row[5], 0))
    return rowData

# 处理表
def handle_data(filename, data:Book):
    # 读取excel中的第一个表
    table = data.sheets()[0] 
    nrows = table.nrows
    ncols = table.ncols
    # 读取表头数据
    fir_col =  table.row_values(0)
    header = {}
    if fir_col:
        for i in range(0, ncols - 1):
            header[str(i)] = fir_col[i]
        print("{} - 表头: {}".format(filename, fir_col))

    list =[]
    # 处理其他行的内容
    for rownum in range(1,nrows): 
        row = table.row_values(rownum)
        if row:
            rowdata = handle_row(filename, row)
            list.append(rowdata)

    print(list)



# 打开当前文件夹下的所有excel文件
def read_curr_dir():
    files = os.listdir('.')
    xlsfiles = []
    for f in files:
        if f.endswith('.xls') or f.endswith('.xlsx'):
            xlsfiles.append(f)
    print(xlsfiles)
    
    for xlsfile in xlsfiles:

        data = open_excel(xlsfile)
        if not data:
            print("data is null : {}".format(xlsfile))
            continue

        handle_data(xlsfile, data)

if __name__ == '__main__':
    read_curr_dir()
