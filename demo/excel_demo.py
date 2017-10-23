# coding=utf-8
# __author__='Administrator'

import xlrd


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
    ncols = table.ncols  # 列数
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
def read_excel(file, row_start=0, col_index=0, sheets_index=1):
    data = open_excel(file)
    table = data.sheets()[sheets_index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    for row in range(row_start, nrows):
        row_val = table.row_values(row)
        print row_val


# write data to the file
def write_excel(file):
    pass


# update the data to the file
def update_excel(file, row_index, col_index, data):
    pass


# check the data to the file
def check_excel(file, row_index, col_index):
    pass


if __name__ == "__main__":
    file = "excel_demo.xlsx"
    read_excel(file, 90)
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
