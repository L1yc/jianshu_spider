# <center>简书_spider</center>

## 项目说明
<p>此项目是通过爬取简书全站，学习scrapy框架，对scrapy有一个初步的认识。</p>

<P>大家一起学习一起交流</p>


##创建过程

+ scarpy startproject XXX
+ scrapy genspdier `-t crawl` XXX domain

###主要步骤
1.数据库操作。

'''python  
	连接 db = pymysql.connect(**kwards)  
	创建 cursor = db.cursors()  
	执行 cursor.execute(sql)   
	提交 db.commit()
'''

	