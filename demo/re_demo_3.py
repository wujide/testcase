# coding=utf-8
# __author__='Administrator'
import re
phone_num =13800138048

reg = r'&captcha=(\d{4})&captCode=(.*?)&isRegisted=(\d)'
reg2 = r'phoneNum=13800138048&captcha=(.*?)&captCode=(.*?)&isRegisted=(\d)'
pattern = r'发送验证码执行完毕phoneNum=\\['+'13800138048'+']'+ r'verifCode='+r'[+(\d?)]'
pattern1 = r"发送验证码执行完毕phoneNum=\[13800138048\]verifCode=[(\d?)]"
pattern2 = r"发送验证码执行完毕phoneNum=\[13800138048\]verifCode=\[(.*?)\]"
pattern22 = r"发送验证码执行完毕phoneNum=\[" + str(phone_num) + r"\]" + r"verifCode=\[(.*?)\]"

pattern3 = "发送验证码执行完毕phoneNum=\[" + str(phone_num) + "\]" + "verifCode=\[(.*?)\]"
print pattern3
result = '[http-bio-8380-exec-7]-2017-09-27 16:13:47,531  INFO VerifCodeServiceImpl:175 - 发送验证码执行完毕phoneNum=[13800138048]verifCode=[8696]'
data = re.findall(pattern3, result)
print "data:", data

