# coding=utf-8
# __author__='wujide'
import xlwt


# 6 位码
def order_no_generator(start, end):
    order_no = []
    for i in range(start, end):
        order_no.append(i)
    return order_no


def row_value(start, end):
    order_no_pre = '12345678901234567890xx'
    ty_serial_no_pre = 'demoINVEST201710xxxx'
    # start = 100000,
    no_post = order_no_generator(start, end)
    post = str(no_post.pop(0))
    order_no = order_no_pre + post
    ty_serial_no = ty_serial_no_pre + post
    order_time = '2017-10-25 09:00:00'
    pay_time = '2017-10-25 09:00:00'
    buy_amount = 1000
    interest_base = 7.77
    product_no = str(0217100034)
    product_code = str(0217100034)
    product_name = u'性能与压力测试产品'
    customer_id = str(10000000000040)
    customer_name = u'python写入'
    order_apply_status = 5
    order_apply_time = '2017-10-25 09:00:00'
    order_pay_status = 1
    pay_type = 1
    login_type = 0
    interest_day = 1
    sale_out_date = '2017-10-25 00:00:00'
    interest_date = '2017-10-26 00:00:00'
    end_time = '2017-10-27 00:00:00'
    repayment_date = '2017-10-27 00:00:00'
    is_tran_register = 1
    source_id = 'QJS'
    create_time = '2017-10-25 09:00:00'
    modify_time = '2017-10-25 09:00:00'
    row_val = [order_no, ty_serial_no, order_time, pay_time, buy_amount, interest_base,
               product_no, product_code, product_name, customer_id, customer_name, order_apply_status,
               order_apply_time, order_pay_status, pay_type, login_type, interest_day, sale_out_date,
               interest_date, end_time, repayment_date, is_tran_register,
               source_id, create_time, modify_time]
    return row_val


# write data to the file
def write_excel_qjs_customer_order(row):
    wbk = xlwt.Workbook()  # 创建工作簿
    sheet1 = wbk.add_sheet('sheet1')  # 创建sheet
    row0 = ['order_no', 'ty_serial_no', 'order_time', 'pay_time', 'buy_amount', 'interest_base',
            'product_no', 'product_code', 'product_name', 'customer_id', 'customer_name', 'order_apply_status',
            'order_apply_time', 'order_pay_status', 'pay_type', 'login_type', 'interest_day', 'sale_out_date',
            'interest_date', 'end_time', 'repayment_date', 'is_tran_register',
            'source_id', 'create_time', 'modify_time']
    # 生成第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])
    # order_no_pre = '12345678901234567890xx'
    # ty_serial_no_pre = 'demoINVEST201710xxxx'
    # no_post = order_no_genter(100000, 1000100)
    for i in range(1, row + 1):
        row_val = row_val(100000, 1000100)
        for col in range(0, len(row0)):
            sheet1.write(i, col, row_val[col])
    wbk.save('qjs_customer_order.xls')  # 保存文件

    '''
        post = str(no_post.pop(0))
        order_no = order_no_pre + post
        ty_serial_no = ty_serial_no_pre + post
        row_val = [order_no, ty_serial_no]
    '''


if __name__ == '__main__':
    write_excel_qjs_customer_order()
