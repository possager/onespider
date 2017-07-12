#_*_coding:utf-8_*_

def get_content_block(xpath_content,xpath_title):
    list_content=xpath_content.split('/')
    list_title=xpath_title.split('/')
    num=0
    xpath_content_list=[]
    while list_content:
        this_div=list_content.pop(1)
        if list_title:
            this_div2=list_title.pop(1)
            if this_div2==this_div:
                num+=1
                xpath_content_list.append(this_div)
                continue
            else:
                break
    xpath_content_str=''
    for tag in xpath_content_list:
        xpath_content_str=xpath_content_str+'/'+tag

    return xpath_content_str

    #/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p
    #/html   /body   /div[3]/div[2]/div   /div   /div   /div   /div   /div[1]/h1
    #/html   /body   /div[3]/div[2]/div   /div   /div   /div   /div
    #/html/body/div[3]/div[2]/div/div/div/div/div/div[1]/h1
    #/html[1]/body[1]/div[1]/table[1]/tr[1]/td[1]/table[4]/tr[1]/td[1]/table[1]/tr[2]/td[1]/table[1]/tr[1]/td[1]/table[1]/tr[1]/td[1]/table[1]/tr[4]/td[1]/p
    #/html[1]/body[1]/div[1]/table[4]/tr[1]/td[1]/table/tr


if __name__ == '__main__':
    xpath1='/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p'
    xpath2='/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1'
    print get_content_block(xpath_content=xpath1,xpath_title=xpath2)