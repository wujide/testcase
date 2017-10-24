# coding=utf-8
# __author__='Administrator'

import xlrd
import xlwt
from xlutils.copy import copy


# open the excel file
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


# 根据索引获取Excel表格中的数据   colnameindex：表头列名所在行  ，by_index：表的索引
def excel_table_byindex(file, colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    row_val = table.row_values(colnameindex)  # 第一行的数据，len(row_val) 也即知道了列数
    list = []
    for rownum in range(0, nrows):
        row = table.row_values(rownum)
        # print row
        if row:
            app = {}
            for i in range(len(row_val)):
                app[row_val[i]] = row[i]
            list.append(app)
    return list


# read the file
def read_excel(file, row_start=0, sheets_index=0):
    data = open_excel(file)
    table = data.sheets()[sheets_index]
    nrows = table.nrows  # 行数
    for row in range(row_start, nrows):
        row_val = table.row_values(row)
        print row_val


# write data to the file
def write_excel():
    wbk = xlwt.Workbook()  # 创建工作簿
    sheet1 = wbk.add_sheet('sheet1')  # 创建sheet
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
    status = [u'预订', u'出票', u'退票', u'业务小计']
    # 生成第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])
    # 生成第一列和最后一列(合并4行)
    i, j = 1, 0
    while i < 4 * len(column0) and j < len(column0):
        sheet1.write_merge(i, i + len(status)-1, 0, 0, column0[j])  # 第一列
        sheet1.write_merge(i, i + len(status)-1, len(row0)-1, len(row0)-1)  # 最后一列"合计"
        i += len(status)
        j += 1
    sheet1.write_merge(4 * len(column0)+1, 4 * len(column0)+1, 0, 1, u'合计')
    # 生成第二列
    col_2 = 0
    while col_2 < 4 * len(column0):
        for j in range(0, len(status)):
            sheet1.write(j + col_2 + 1, 1, status[j])
        col_2 += len(status)
    wbk.save('write_excel.xls')  # 保存文件


# update the data to the file
def update_excel(file, row_index, col_index, data):
    pass


# check the data to the file
def check_excel(file, row_index, col_index):
    pass


if __name__ == "__main__":
    file = "excel_demo.xlsx"
    # read_excel(file, 90)
    write_excel()
#    for i in excel_table_byindex(file):
#        print i


'''





data = xlrd.open_workbook('excel_demo.xlsx')  # 打开Excel文件读取数据
# table = data.sheet_by_name(u'Sheet1')  # 通过名称获取工作表
# table = data.sheet_by_index(0) # 通过索引顺序获取
table = data.sheets()[0]  # 通过索引顺序获取
nrows = table.nrows
ncols = table.ncols
print "nrows, ncols=", nrows, ncols

for index in range(nrows):
    print table.row_values(index)
    # print str(int(table.row_values(index)[0])) + ":" + str(int(table.row_values(index)[1]))
    # table.put_cell(index, 1, 1, str(int(table.row_values(index)[1])+1), 0)

# 单元格
cell_A1 = table.cell(0, 0).value
cell_D3 = table.cell(2, 3).value

print cell_A1, cell_D3

table.put_cell(1, 3, 1, "03", 0)
print table.cell(1, 3).value
print table.cell(2, 3).value
print table.cell(2, 3)

'''
