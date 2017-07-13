#_*_coding:utf-8_*_
import pymongo
from operator import itemgetter

#这里边所有的调整都不会和机器学习模型结束后的结果一样.

# client=pymongo.MongoClient('localhost',27017)#之前测试用的
# thisCOL=client['xpath1']
# thisDOC=thisCOL['allxpath1']


def getxpath(response_list):
    # url='http://sn.newssc.org/system/20170418/002159156.html'.replace('.','_')#之前测试的时候用的,后来datalist就该成了response_list
    # datalist=thisDOC.find({'url':url},{'_id':0})
    # for i in datalist:
    #     for j in i['data']:
    #         print j

    # response_list=datalist[0]['data']
    # PN_list=[]
    # TL_list=[]
    # for node_inf in response_list:
    #     PN_list.append(node_inf['PN'])
    #     TL_list.append(node_inf['TL'])
    # TL_list_sort= sorted(TL_list)[-10:]
    # PN_list_sort= sorted(PN_list)[-10:]
    # print TL_list_sort
    # print PN_list_sort
    # PN_xpath_list=[]
    # TL_xpath_list=[]
    # while TL_list_sort:
    #     num=TL_list_sort.pop()
    #     PN_list

    result_list_PN=sorted(response_list['data'],key=itemgetter('PN'),reverse=True)
    print result_list_PN
    result_list_TL=sorted(response_list['data'],key=itemgetter('TL'),reverse=True)
    print result_list_TL

    result_dict={}
    for i in result_list_PN[0:10]:#这个部分的功能还是有一个问题,因为这里变的流程是根据xpath出现的频率来统计的,里边有可能会出现错误情况:几个个长度都不是太长并且不是正文的xpath,但是出现的次数比较多,所以就会让这个出现频率特别高的
        #成为主界面.
        if i['has_url']==0 and i['TL']>1:#后来又发现有一个没有长度的变量突然冒了出来所以添加这一个功能
            keys1=result_dict.keys()
            if i['xpath'] in keys1:
                result_dict[i['xpath']]+=1
            else:
                result_dict[i['xpath']]=1
    for i in result_list_TL[0:10]:#没有找到内容的网页是因为这个网页中的空格太多了,而标点符号几乎一个偶读没有,所以应该添加一个标点符和内容有关的变量来作为判断变量
        keys1=result_dict.keys()
        if i['has_url']==0 and i['TL']>1:
            if i['xpath'] in keys1:
                result_dict[i['xpath']]+=1
                # result_dict['xpath']=i['xpath']
                # result_dict['repeat_num']=result_dict[i['xpath']]
            else:
                result_dict[i['xpath']]=1
            # result_dict['xpath']=i['xpath']
            # result_dict['repeat_num']=result_dict[i['xpath']]
    print result_dict

    for iii in result_dict.iteritems():
        print iii
        print len(iii)

    result_dict2=sorted(result_dict.iteritems(),key=lambda x:x[1],reverse=True)

    # print result_dict2
    return result_dict2[0]


# def get_value(data):
#     print

if __name__ == '__main__':
    xpath=getxpath('none')
    print xpath