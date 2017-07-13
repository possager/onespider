#_*_coding:utf-8_*_
import re

def find_time(referenceBlock_str):
    Re_find_time=re.compile(r'20[0-9]{2}[\s\S][0-1]?[0-9]{1}([\s\S]{1,2}[0-2]\\d[\s\S[0-5]\\d([\s\S][0-5]\d)?)*')
    publish_time=Re_find_time.findall(referenceBlock_str)

    return publish_time

if __name__ == '__main__':
    strq='2012-07-09,'
    print find_time(strq)