#_*_coding:utf-8_*_
import pickle


# file1='/media/liang/3804CCCA04CC8C76/project/YFzhongxin/xpath_test/xpath.pkl'
# file1_data=open(file1,'r+')
# web_dict=pickle.load(file1_data)
# for i in web_dict.child.keys():
#     if i.name=='title':
#         print 'Find it!!  xpath is --------',i.xpath





def getchild(pickle_dict):#用来获取title模块的
    if pickle_dict.name=='title':
        try:
            title_in_getchild=pickle_dict.content.pop()
            print 'find it! the title is ------',title_in_getchild,'the xpath is -----------',pickle_dict.xpath
            return title_in_getchild
        except Exception as e:
            print e
    else:
        for one_key in pickle_dict.child.keys():
            title_in_getchild=getchild(pickle_dict.child[one_key])
            if title_in_getchild:
                return title_in_getchild
        # return title_in_getchild




def dealcontent(webpage_class):
    content=webpage_class.content
    if content:
        for content_num in range(len(content)):
            content[content_num]=content[content_num].lstrip('\t').lstrip('\n').lstrip(' ').lstrip('\r').rstrip('\t').rstrip('\n').rstrip(' ').rstrip('\r')

        # content=content.strip('\t').strip('\n').strip(' ')
        webpage_class.contetnt=content
        for one_key in webpage_class.child.keys():
            dealcontent(webpage_class.child[one_key])


def find_compare_list(title_str,webpage_class,maybe_content_list):
    this_content_len=len(title_str)
    if webpage_class.content:
        for one_content in webpage_class.content:
            if len(one_content)<=this_content_len+2 and len(one_content)>5:
                if webpage_class.has_url == 0:
                    maybe_content_list.append({one_content:webpage_class.xpath})

    for one_key in webpage_class.child.keys():
        find_compare_list(title_str,webpage_class.child[one_key],maybe_content_list)
    return maybe_content_list,title_str


def find_compare_title(title,webpage_class,maybe_content_list=[]):#这个这个maybe_content_list本来就是空的,函数内部会再次应用它,所以可以不用赋值
    maybe_content_list,title_str=find_compare_list(title_str=title,webpage_class=webpage_class,maybe_content_list=maybe_content_list)
    xpath_list=[]#7-13日添加
    for one_content in maybe_content_list:
        if one_content.keys()[0] in title_str:
            index_in_for=title_str.index(one_content.keys()[0])
            print index_in_for
            if index_in_for<1:
                print 'find it ,------------------the title is (in find_compare_title)-------',one_content.keys()[0]
                print 'the xpath is ',one_content.values()[0]
                print index_in_for
                # return one_content#后来发现这里边的有问题,因为在文章内容中的也有和标题一样的句子,如网页http://m.taihainet.com/news/twnews/twdnsz/2006-04-05/173.html里边就有和标题一样的句子.
            #所以这里设计成一个列表将里边所有的xpath比较一下,选长度最短的那一个,至少目前网站是可以解决的.
                xpath_list.append(one_content)
    #7-13处理xpath部分,选出长度最短的:
    num=500#500是随便取的,目的是为了获得长度最小的xpath,一般xpaht的长度都不会大于500
    target_xpath=''
    while xpath_list:
        xpath_in_while=xpath_list.pop()
        if num>len(xpath_in_while.values()[0]):
            num=len(xpath_in_while.values()[0])
            target_xpath=xpath_in_while
    return target_xpath

#-----------------------------------------------------------------
#解释,这里的执行流程是首先用dealcontent,吧数据先清理一遍,之后再用find_compare_list将里边的可能是标题的内容选出来,之后再将选出来的所有可能是集合
#的元素全部用最后的find_compare_title这个函数来处理,找出其中匹配上的第一个元素,就是我要的目标
#_________________________________________________________________


def get_title(thisclass):
    dealcontent(thisclass)
    title_str=getchild(thisclass)
    title_and_xpath=find_compare_title(title=title_str,webpage_class=thisclass)
    print 'finish'
    return title_and_xpath