#_*_coding:utf-8_*_
import re

def find_time(referenceBlock_str):
    # Re_find_time=re.compile(r'20[0-9]{2}[\s\S][0-1]?[0-9]{1}([\s\S]{1,2}[0-2]\d[\s\S[0-5]\d([\s\S][0-5]\d)?)*?')
    Re_find_time2=re.compile(r'[1,2]\d{3}[ \-\:\/]{1,2}[0,1]\d[ \-\:\/]{1,2}\d{1,2}[ \-\:\/]{0,3}\d{0,2}[ \-\/\:]{1,2}\d{0,2}[ \-\/\:]{1,2}\d{0,2}')
    # Re_find_time3=re.compile(r'[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]')
    # Re_find_time4=re.compile(r'1\d{3}[ \-\:\\\/]{0,2}')
    # Re_find_time_taoge=re.compile(r'\d{4}([年|\/|\/|\.|\s|\-]*?)\d{1,2}([月|\/|\/|\.|\s|\-]*?)\d{1,2}([日|\/|\/|\.|\s|\-]*?)\s*?\d{1,2}([\:|时|\-]*?)\d{1,2}([\:|分|\-]*?)\d{1,2}([\:|秒|\-]?)')
    Re_find_time_taoge2=re.compile(r'\d{4}?([年|\/|\/|\.|\s|\-]*?)\d{1,2}([月|\/|\/|\.|\s|\-]*?)\d{1,2}([日|\/|\/|\.|\s|\-]*?)\s*?\d{1,2}([\:|时|\-]*?)\d{1,2}([\:|分|\-]*?)\d{1,2}([\:|秒|\-]?)')
    publish_time=Re_find_time_taoge2.search(referenceBlock_str).group()


    return publish_time

if __name__ == '__main__':
    strq='2012-07-09 12:12:12'
    print find_time(strq)