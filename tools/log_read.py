# coding=utf-8
# __author__='wujide'

import re


# use re to get the data needed
def log_read(pattern, data):
    # pattern = r'&captcha=(\d{4})&captCode=(.*?)'
    data = re.findall(pattern, data)  # <type 'list'>
    return data


if __name__ == "__main__":
    pat = r'&captcha=(.*?)&captCode=(.*?)&isRegisted=(\d)'
    res = '[http-bio-8380-exec-10]-2017-09-26 21:39:23,741  INFO VerifCodeServiceImpl:72 - phoneNum=13800138048&captcha=6130&captCode=57fd2f48c9a345708d0f6d1e876ad27d&isRegisted=1'
    print log_read(pat, res)
