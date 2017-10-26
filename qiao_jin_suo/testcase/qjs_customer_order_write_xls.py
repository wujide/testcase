# coding=utf-8
# __author__='wujide'
import xlwt


# 6 位码
def order_no_gen(start, end):
    order_no = []
    for i in range(start, end):
        order_no.append(i)
    return order_no


# write data to the file
def write_excel_qjs_customer_order():
    wbk = xlwt.Workbook()  # 创建工作簿
    sheet1 = wbk.add_sheet('sheet1')  # 创建sheet
    row0 = ['order_no', 'ty_serial_no', 'order_time', 'pay_time', 'buy_amount', 'interest_base',
            'product_no', 'product_code', 'product_name', 'customer_id', 'customer_name','order_apply_status',
            'order_apply_time', 'order_pay_status', 'pay_type', 'login_type', 'interest_day', 'sale_out_date',
            'interest_date', 'end_time', 'repayment_date', 'is_tran_register',
            'source_id', 'create_time', 'modify_time']
    # 生成第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])
    order_no_pre = '12345678901234567890xx'
    ty_serial_no_pre = 'demoINVEST201710xxxx'
    no_post = order_no_gen(100000, 1000100)
    for i in range(1, 101):
        post = str(no_post.pop(0))
        order_no = order_no_pre + post
        ty_serial_no = ty_serial_no_pre + post
        data = []
        data.append(order_no)
        data.append(ty_serial_no)
        for col in range(0, 2):
            sheet1.write(i, col, data[col])
    wbk.save('qjs_customer_order.xls')  # 保存文件


if __name__ == '__main__':
    write_excel_qjs_customer_order()