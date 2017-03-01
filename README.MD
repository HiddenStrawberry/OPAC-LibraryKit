Huiwen OPAC LibraryKit
----------------------

----------
这个Library Kit用来在未授权直接访问网上图书馆数据时使用。用来作为中间件获取江苏汇文软件有限公司的OPAC V5.0.1.0224图书馆系统数据。

使用方法
----


----------

 1. 编辑Config.py
 更改参数opac的地址和opac网页编码
 2. 打开main.py

Example
-------


----------


    test=search('Python')
    for each in test:
    	get_item(each,1)

out：

    题名/责任者: Python 3基础教程
    出版发行项: 北京:人民邮电出版社,2016
    ISBN及定价: 978-7-115-43487-6/CNY42.00
    载体形态项: 278页:图;26cm
    并列正题名: Python 3 course
    个人责任者: 邓英
    个人责任者: 夏帮贵
    学科主题: 软件工具
    中图法分类号: TP311.561
    一般附注: 工业和信息化“十三五”人才培养规划教材
    提要文摘附注: 本书注重基础、循序渐进，系统地讲述了Python程序设计开发的相关知识。全书共分8章，涵盖了Python开发环境及工具、编程基础、程序流程控制、函数与模块、面向对象编程、异常处理、数据库编程和tkinter GUI编程等内容。
    ……


----------

    
    test=search('Python')
    for each in test:
    	print get_item(each,0) #这是一个字典结构，key为缩写，value为内容
   out：
   

    {u'cbfxx:': u'\u5317\u4eac:\u4eba\u6c11\u90ae\u7535\u51fa\u7248\u793e,2016', u'ztfflh:': u'TP311.561', u'tywzfz:': u'\u672c\u4e66\u6ce8\u91cd\u57fa\u7840\u3001\u5faa\u5e8f\u6e10\u8fdb\uff0c\u7cfb\u7edf\u5730\u8bb2\u8ff0\u4e86Python\u7a0b\u5e8f\u8bbe\u8ba1\u5f00\u53d1\u7684\u76f8\u5173\u77e5\u8bc6\u3002\u5168\u4e66\u5171\u52068\u7ae0\uff0c\u6db5\u76d6\u4e86Python\u5f00\u53d1\u73af\u5883\u53ca\u5de5\u5177\u3001\u7f16\u7a0b\u57fa\u7840\u3001\u7a0b\u5e8f\u6d41\u7a0b\u63a7\u5236\u3001\u51fd\u6570\u4e0e\u6a21\u5757\u3001\u9762\u5411\u5bf9\u8c61\u7f16\u7a0b\u3001\u5f02\u5e38\u5904\u7406\u3001\u6570\u636e\u5e93\u7f16\u7a0b\u548ctkinter GUI\u7f16\u7a0b\u7b49\u5185\u5bb9\u3002', u'grzrz:': u'\u590f\u5e2e\u8d35', u'ybfz:': u'\u5de5\u4e1a\u548c\u4fe1\u606f\u5316\u201c\u5341\u4e09\u4e94\u201d\u4eba\u624d\u57f9\u517b\u89c4\u5212\u6559\u6750', u'ztxtx:': u'278\u9875:\u56fe;26cm', u'blztm:': u'Python 3 course', u'xkzt:': u'\u8f6f\u4ef6\u5de5\u5177', u'ISBNjdj:': u'978-7-115-43487-6/CNY42.00', u'tmzrz:': u'Python 3\u57fa\u7840\u6559\u7a0b'}


----------

    print getselect(display_pm(ourl)) #返回一个字典结构，含有页面所有的简单搜索选项参数，结构为{参数名：[选项名],[选项值]}
out：

    strSearchType
    title 题名 author 责任者 keyword 主题词 isbn ISBN/ISSN asordno 订购号 coden 分类号 callno 索书号 publisher 出版社 series 丛书名 tpinyin 题名拼音 apinyin 责任者拼音  
     
    sort
    CATA_DATE 入藏日期 M_TITLE 题名 M_AUTHOR 责任者 M_CALL_NO 索书号 M_PUBLISHER 出版社 M_PUB_YEAR 出版日期  
     
    displaypg
    20 20条 30 30条 50 50条 100 100条  
     
    match_flag
    forward 前方一致 full 完全匹配 any 任意匹配  
     
    dept
    ALL 所有校区 00 总馆 01 北圩 02 晓庄 03 方山 
    
    {u'strSearchType': [[u'title', u'author', u'keyword', u'isbn', u'asordno', u'coden', u'callno', u'publisher', u'series', u'tpinyin', u'apinyin'], [u'\u9898\u540d', u'\u8d23\u4efb\u8005', u'\u4e3b\u9898\u8bcd', u'ISBN/ISSN', u'\u8ba2\u8d2d\u53f7', u'\u5206\u7c7b\u53f7', u'\u7d22\u4e66\u53f7', u'\u51fa\u7248\u793e', u'\u4e1b\u4e66\u540d', u'\u9898\u540d\u62fc\u97f3', u'\u8d23\u4efb\u8005\u62fc\u97f3']], u'sort': [[u'CATA_DATE', u'M_TITLE', u'M_AUTHOR', u'M_CALL_NO', u'M_PUBLISHER', u'M_PUB_YEAR'], [u'\u5165\u85cf\u65e5\u671f', u'\u9898\u540d', u'\u8d23\u4efb\u8005', u'\u7d22\u4e66\u53f7', u'\u51fa\u7248\u793e', u'\u51fa\u7248\u65e5\u671f']], u'displaypg': [[u'20', u'30', u'50', u'100'], [u'20\u6761', u'30\u6761', u'50\u6761', u'100\u6761']], u'match_flag': [[u'forward', u'full', u'any'], [u'\u524d\u65b9\u4e00\u81f4', u'\u5b8c\u5168\u5339\u914d', u'\u4efb\u610f\u5339\u914d']], u'dept': [[u'ALL', u'00', u'01', u'02', u'03'], [u'\u6240\u6709\u6821\u533a', u'\u603b\u9986', u'\u5317\u5729', u'\u6653\u5e84', u'\u65b9\u5c71']]}


----------


>这段代码适用于且可能不仅适用于[OPAC V5.0.1.0224][1]    
有任何问题请联系作者，QQ：1317171753

 - 本项目的参数部分使用了[cleverdeng/pinyin.py][2]的拼音转缩写工具


  [1]: http://lib2.shutcm.edu.cn:8080/opac/search.php
  [2]: https://github.com/cleverdeng/pinyin.py
