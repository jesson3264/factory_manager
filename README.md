
# factory-manage
基于Django的工厂后台管理系统，主要包含以下功能：
- 员工管理
- 考勤
- 工资
- 订单
- 生产日报
- 仓库
- 采购
- 设备
- 公告

## 技术
  基于 Django 2.2, bootstrap3.3.7开发


## 联系我
    jesson3264@163.com
    wx: coder-jesson
	
## 主页
### 未登录
以下截图是个没有用户登录的一个主页，只显示公司的公告信息一些，以及轮播的宣传图片。
![alt text](images/nologin.png)



### 登录
登录之后，导航栏会根据不用的用户角色显示不同的功能。以下是一个经理角色登录之后显示的内容，功能最全。
包含以下核心功能：
- 员工
- 考勤
- 工资
- 生产日报
- 仓库
- 采购
- 设备
- 公告
![alt text](images/login.png)

以下是一些详细介绍。

## 员工 
员工栏，包含
- 员工类型
- 全体员工
- 新增员工
- 新增职位

![](images/yuangong.png)


### 员工类型
员工类型显示该系统所有的员工类型
![](images/yuangongleixing.png)



### 全体员工
全体员工功能可以显示公司所有的员工，具备翻页功能

![](images/quanbuyuangong.png)


### 新增员工
当公司有新员工入职时，新增员工功能就起作用了。

新增员工时，可以选择员工的职位，通过职位来控制员工的权限，其他就是一些员工的必备信息了。其中电话，身份证号会做校验，避免输入错误的信息。
![](images/yg-xinzeng.png)


 ### 新增职位

 丰富公司员工的各种角色

![](images/yg-xzzw.png)

## 考勤

![](images/kq.png)


### 新增考勤

实际的公司后台管理系统，考勤信息往往是从考勤设备或者第三方的考勤系统中来。比如打卡机，或者企微类的在线打卡系统。
所以这里模拟的是从其他系统上导入考勤信息。

这里主要是一个补卡的功能。
![](images/kq-xz.png)

### 查找
查找功能可以根据姓名和日期进行查找。

![](images/kq-cz1.png)



## 工资

![](images/gz-1.png)


### 查找
查找功能可以根据工资相关信息选择不同类型的关键字进行查找工资信息

![](images/gz-cz1.png)



## 订单

订单支持新增和查找，这也是常见的功能。

![](images/dd-all.png)

### 订单新增
![](images/dd-xz1.png)

### 订单查找

![](images/dd-cz1.png)



## 生产日报

生产日报支持新增和查找，功能中规中矩
![](images/scrb-all.png)


### 生产日报新增
![](images/scrb-xz1.png)

### 生产日报查找

![](images/scrb-cz1.png)



## 仓库
仓库主要是管理各种产品和原料
功能包含： 产品类型、原料类型、产品日报、原料日报
![](images/ck-all.png)

### 产品类型
![](images/ck-add.png)


### 原料类型
![](images/ck-yllx.png)

### 产品日报
![](images/ck-cprb.png)

### 原料日报
![](images/ck-ylrb.png)



## 采购

![](images/cg-all.png)

### 申请
![](images/cg-sq.png)

### 待批准
![](images/cg-dpz.png)
### 待采购
![](images/cg-dcg.png)

### 采购记录
![](images/cg-ls.png)



## 设备

![](images/sb-all.png)

### 设备档案
![](images/sb-sbda.png)

### 保养记录
![](images/sb-byjl.png)


### 报修
![](images/sb-bx.png)


### 待维修
![](images/sb-dwx.png)


### 维修记录
![](images/sb-wxjl.png)


## 公告

![](images/gg.png)

### 新增公告
![](images/gg-xz.png)

### 通知列表
![](images/gz-lb.png)




