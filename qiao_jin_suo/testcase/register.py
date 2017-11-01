# coding=utf-8
# __author__='wujide'
from time import ctime
from interface_test_class import InterfaceTest
from login_imgCaptcha import imgCaptcha
from login_validImgKaptcha import validImgKaptcha
from login_smsCaptcha import smsCaptcha
from login_register import login_register


def register(mobile):
    print "started at %s" % ctime()
    # https://api.gocfae.com/cust/login/ 图形码获取
    img_Captcha = imgCaptcha()
    # validImgKaptcha 图形码验证
    validImgKaptcha()
    # 短信验证码验证https://api.gocfae.com/cust/login/smsCaptcha
    smsCaptcha(mobile)
    # https://api.gocfae.com/cust/login/register 注册
    login_register(mobile)
    # sendMsgByPreBind 绑卡发送验证码 -》"orderNo":"1710312229467960001118114776"}
    orderNo = sendMsgByPreBind()
    # card_bindCard 完成注册 https://api.gocfae.com/cust/card/bindCard


if __name__ == '__main__':
    print register(13800138008)


