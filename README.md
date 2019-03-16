# <center>简书_spider</center>

## 项目说明
<p>此项目是通过爬取简书全站，学习scrapy框架，对scrapy有一个初步的认识。</p>

<P>大家一起学习一起交流</p>


##创建过程

+ scarpy startproject XXX
+ scrapy genspdier `-t crawl` XXX domain

###主要步骤   

1.数据库操作。     
     
    1.连接 db = pymysql.connect(**kwards)     
    2.创建 cursor = db.cursors()    
    3.执行 cursor.execute(sql)     
    4.提交 db.commit()      

使用twisted进行异步存储，加快爬取效率  
```python  
from twisted.enterprise import adbapi

db = adbapi.ConnectionPool(mysql,**params)

db.runInteraction()

```

	