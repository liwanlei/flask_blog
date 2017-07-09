# 使用flask 实现blog，数据库是sqlite
# 目前实现注册，登录，评论，写博客，编辑资料,修改头像，编辑博客,回复，缓存等功能
# 开发api接口，目前实现注册，查询文章，查询分类文章，查询标签文章的api接口。

# 使用方法就是git clone  然后进入，现在的数据库是sqlite，使用命令行
## python db_migrate db init 
## 初始化我们的数据库，这里呢，我在app下面的__init__文件配置了
## os.environ['MODE'] = 'dev'
## 所以呢，我们这个数据库默认的就是dev的数据库，然后用
## python db_migrate db migrate
## python db_migrate db upgrade
## 这样我们可以去查看我们的数据库，  在config目录就有我们的数据库，而且我们可以看到我们的数据表。
##   然后我们使用命令 python manager.py run 启动我们的程序， 启动后如下面的图所示。

## 下面的结构图如图所示：
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/jiegou.png)
## 实际运行效果，后期会做一些优化，展示的界面如下图所示。可能部分界面不太兼容，目前水平有限。
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/denglu.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/re.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/shouye.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/sousuojiemian.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/post.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/re.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/new_post.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/bianji.png)
![Alt text](https://github.com/liwanlei/flask_blog/blob/master/images/cenner.png)

# 基于ubuntu +Ningx+uswgi的部署已经完成，配置文件也上传，并且可以实现部署，然后做自动化，第一个flask 自己写的东西已经完成差不多了。
##  我这里有博客去介绍了。http://www.cnblogs.com/leiziv5/p/7137277.html
## 然后我们在命令行去启动我们uwsgi 和nginx就可以，
## 笔者也遇到了很多的502错误，这里呢 我们去看下/var/log/nginx/arror.log 找到最新一次的请求，我们去看下我们最新的请求的文件的的报错就可以，
##  我遇到的是权限不足，  但是我看了下uwsgi和nginx的配置中间出的问题，nginx指向是文件来确定和uwsgi的通信 uwsgi是通过端口号，所以我后来就都改成了端口号，就可以了，还有的有些报错呢，是因为我们在nginx缺少什么配置，我的完整的配置就是在hellowflask_nginx.conf 文件下。
