# 轻量级办公平台Sandbox
### 本项目功能实现和代码逻辑上都不够完善，项目不再更新维护。新项目地址：https://github.com/RobbieHan/sandboxMP
### 系统中所演示的数据均系杜撰，并非真实数据，包括单位名称、人名、地名和通信方式。
sandbox是一个基于django框架开发的轻量级办公平台，主要模块有：权限控制、资产（库存）管理、设备管理、客户信息管理和工单流程管理，其目的在于建立一套规范化、统一化和清晰化的标准服务流程，能够清晰的处理、记录和追踪服务流程，同时依赖于工单流程模块，建立技术服务文档共享库，让技术人员相互协作，分享经验，提升服务技术水平。
这套系统的开发主要是为了规范当前公司服务流程，改变服务混乱，项目多人多次服务无交接的问题，同时将公司资产（库存）和销售的设备一起做了集中管理和服务跟踪。
目前公司主要是对外销售安全产品和安全服务，作为一个小型乙方公司，上一套OA系统太过繁重，所以就自己动手来做了这么一套轻量级办公系统。
# 1 功能介绍
## 1.1 权限管理功能介绍
系统权限是采用基于角色组的权限配置，根据用户角色组权限动态生成导航菜单<br>
图1：基于角色组的权限管理，权限分明，各司其职<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/001.jpg)<br>
## 1.2 客户信息管理
客户信息管理用于建立客户信息数据库，避免因销售离职，遗失客户信息而给公司带来的损失<br>
图2：建立客户信息库，客户是公司的生存根本<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/002.jpg)<br>
## 1.3 资产(库存)管理
资产管理用于资产登记入库，资产流转，信息变更，实时记录资产动向<br>
图3：资产责任到人，避免因多次借用转手造成的资产遗失<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/003.jpg)<br>
## 1.4 设备管理
设备管理用于登记公司销售出去的设备信息，记录设备服务记录<br>
图4：销售设备信息登记<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/004.jpg)<br>
图5：服务跟踪，实时记录，有始有终，拒绝虎头蛇尾<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/004-1.jpg)<br>
## 1.5 工单流程管理
工单流程管理目的在于建立标准化流程服务，让每一次客户服务都有迹可查，长期建立客户服务文档库，努力为客户提供更专业的服务，点滴专注，值得信赖。<br>
图6：工单统计<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/005-1.jpg)<br>
图7：工单列表<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/005-2.jpg)<br>
图8：工单流转，工单详情页，流程记录，文档上传<br>
![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/005-3.jpg)<br>
## 1.6 工单文库管理
工单文库用于分享工单执行过程中上传的记录文档，包括设备的安装调试记录、故障处理报告和项目方案设计文档，用于技术人员之间进行经验分享<br>

![image](https://github.com/RobbieHan/gistandard/blob/18ac4434490d3658b72a4a77ef6656ffad01beed/media/sandbox-image/006.jpg)<br>

笔者是一名信息安全公司从业者，一名小技术工程师，写代码非我本职工作，系统虽然轻量，不过完全是根据公司流程定制开发，可满足目前工作需求。<br>
系统开发使用的是django框架，前端是bootstarp jquery ajax ，图表 echarts<br>
经历一个月的开发周期目前系统已经成功上线运行，同时小范围的提供给同样身为乙方公司的合作伙伴使用了，截至2018年6月30日部署在用共计19套。<br>

# 2 开源声明
对于我来说这套系统是完美的，因为我是根据自己的工作需求亲手打造了它；同时它不是完美的，因为我很业余，它还很小，需要成长，许多功能不够完善，代码逻辑不够清晰。<br>
自在知乎发布文章一周来，很多人关注sandbox，应大家要求，今天将系统开源，希望能够帮到大家，同时也希望大家能够一起完善它，优化它。
项目地址：https://github.com/RobbieHan/gistandard

# 3 安装说明
## 3.1 线上环境部署
 系统运行环境 centos7 python3.6 mysql 5.6, 系统需要安装 docker , docker-compose <br> 
1、下载项目文件到你的系统<br>
```
$ git clone https://github.com/RobbieHan/gistandard.git<br>
```

2、进入项目目录，拷贝和修改配置文件<br>
```
$ cd gistandard
$ mkdir -p /sandbox/nginx 
$ cp config/nginx.conf /sandbox/nginx/
$ cp -r media /sandbox
$ vim /sandbox/nginx/nginx.conf
# 修改nginx配置文件中 server标签下的 server_name 为你系统的地址IP 或域名（sandbox安装完成通过这个地址来访问）
```
3、运行容器
```
$ docker-compose up -d
```
等等等等.....<br>
查看容器运行状态：<br>
```
$ docker-compose ps <br>
       Name                     Command               State         Ports       
--------------------------------------------------------------------------------
gistandard_mysql_1   docker-entrypoint.sh mysql ...   Up      3306/tcp          
gistandard_web_1     bash -c uwsgi config/sandb ...   Up      0.0.0.0:80->80/tcp

```
4、导入数据库文件
```
$ docker cp db_tools/data/basic_data.sql gistandard_mysql_1:/tmp
$ docker-compose exec mysql bash<br>
$ mysql -uddadmin -p1234@abcd.com gistandard < /tmp/basic_data.sql
```

5、访问系统：<br>
http://your_ip   初始用户 admin  密码 !qaz@wsx <br>

## 3.2 本地环境运行
如果只是想查看代码和系统功能，可以在本地windows环境下临时运行项目，或者使用开发工具运行项目<br>
1、从github上下载项目文件到本地，或者使用git克隆项目 <br>
2、在windows上安装python3.6环境（也可以使用python虚拟环境，python环境的安装方法网上很多，这里不再写了）<br>
3、修改gistandard/gistandard/settings.py文件中数据库连接配置DATABASES, 本地运行使用db.sqlite3数据库，内含测试数据 <br>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

4、安装依赖包，打开CMD命令行，进入项目主目录运行下面命令安装依赖包：

**注意：** 
- 本地环境使用的是sqlite3数据库，安装依赖包前可以先将requirements文件中的mysqlclient那一行删掉，这个包是用来连接mysql数据库使用的，通常windows下安装这个包会报错，解决办法我在知乎境部署的文档中都有写过。
- 我windows下使用的是python虚拟环境，所以我下面CMD命令行开头是(gistandard)这个是我虚拟环境的名称，虚拟环境的使用方法也可以网上找下，或者关注我的知乎专栏，环境部署文档中都有介绍。

```
(gistandard) D:\ProjectFile\gistandard>pip install -r requirements
```


5、运行项目，接着第4步，在CMD命令窗口输入项目运行命令：
```
(gistandard) D:\ProjectFile\gistandard>python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
November 05, 2018 - 11:45:37
Django version 1.11.6, using settings 'gistandard.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```

项目已经成功运行，可以通过http://127.0.0.1:8000 访问系统，用户名 admin, 密码: !qaz@wsx <br>
