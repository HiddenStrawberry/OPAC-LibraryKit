Huiwen OPAC LibraryKit
----------------------

----------
这个Library Kit用来在未授权直接访问网上图书馆数据时使用。用来作为中间件爬取江苏汇文软件有限公司的OPAC V5.0图书馆系统。

使用方法
----


----------

 1. 编辑Config.py
 更改参数opac和opac网页编码
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




> 有任何问题请联系作者，QQ：1317171753

