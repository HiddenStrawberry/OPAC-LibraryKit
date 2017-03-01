#encoding=utf8
#Used in SUT
#OPAC v5.0.1.0224
import sys
import threading
import requests
import re
import time
import os.path
from config import *
import HTMLParser
from pinyin import PinYin
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8',)
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
def getselect(html):
    select_option={}
    select_hm=re.findall('<select class="option"(.*?)lect>',html,re.S)
    for each in select_hm:
        name=re.findall('name="(.*?)"',each,re.S)[0]
        p=re.findall('px;">(.*?)</se',each,re.S)[0]
        value=re.findall('value="(.*?)"',p,re.S)
        value_name=re.findall('">(.*?)</option>',p,re.S)
        if len(value)!=len(value_name):
            print name
            raise Exception ("Error 2")
        select_option[name]=[value,value_name]
    return select_option
def display_pm(ourl):
    url=ourl
    searchhm=(requests.get(url+'search.php').text).encode(encoder).decode('utf8').replace('&nbsp;','')
    select_dict=getselect(searchhm)
    print '----------------------------------------'
    print '-------------Parameter------------------'
    for key,values in select_dict.items():
        
        print key
        for each in range(len(values[0])):
            print values[0][each],
            print values[1][each],
        print ' '
        print ' '
    print '----------------------------------------'
def get_item(marc_no,status=0):
    dict={}
    test = PinYin()
    test.load_word('word.data')
    hm=requests.get(ourl+'item.php?marc_no='+str(marc_no)).text.encode(encoder).decode('utf8').replace('&nbsp;','')
    parser = HTMLParser.HTMLParser()
    s1 = parser.unescape(hm)
    static=re.findall('<div id="book_info">(.*?)<div class="clear"></div>',s1,re.S)[0]
    booklist=re.findall('<dl class="booklist">(.*?)</dl>',static,re.S)
    for each in booklist:
        pm=re.findall('<dt>(.*?)</dt>',each,re.S)[0]
        if pm=='':
            continue
        st=re.findall('<dd>(.*?)</dd>',each,re.S)[0]
        try:
            st1=re.findall('>(.*?)</a>',st,re.S)[0]
        except:
            st1=st
        pms=test.hanzi2pinyin_split(string=pm, split="", firstcode=True).replace('/','')
        dict[pms]=st1
        if status==1:
            print pm,
            print st1
    return dict
def search(keyword,strSearchType='title',match_flag='forward'):
    hm=requests.get(ourl+'openlink.php?strSearchType='+str(strSearchType)+'&match_flag='+str(match_flag)+'&historyCount=1&strText='+str(keyword)+'&doctype=ALL&displaypg=100&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL').text.encode(encoder).decode('utf8').replace('&nbsp;','')
    book_list=re.findall('<li class="book_list_info"(.*?)</li>',hm,re.S)
    marc_no=re.findall('php\?marc_no=(.*?)"',str(book_list),re.S)
    return list(set(marc_no))
    '''
    for each in book_list:
        pic=re.findall('<img id="book_img" width="105" height="155" style=" border:1px solid #efefef;" src="http://img7.doubanio.com/mpic/s6476331.jpg">
    '''

get_item('0000194276')

