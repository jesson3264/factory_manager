文档内容包含

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


## 部署
**部署环境和方式（开发软件、需要下载的依赖、数据库导入、配置）**

## 数据库

### 表名: auth_group
它用于管理和定义一组用户的权限
|cid|name|type|notnull|dflt_value|	pk| meaning|
|-----|------|--------|-----|----|----|--|
0|id|INTEGER|1||1| id
1|name|varchar(150)|1||0|组权限名称

### 表名：auth_group_permissions
用来管理 组与权限的关系
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
|0|id|INTEGER|1| |1| id|
|1|group_id|INTEGER|1||0| 组 id
|2|permission_id|INTEGER|1||0| 权限 id

### 表名：auth_permissions
表用于存储权限的定义，它记录了哪些模型和操作（例如添加、修改、删除）与特定的权限相关联
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|id
1|content_type_id|INTEGER|1||0 | 表的外键，表示该权限属于哪个模型（表）
2|codename|varchar(100)|1||0 |权限编码名
3|name|varchar(255)|1||0| 权限名称

### 表名：表名：auth_user
用户信息表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1| 唯一标识
1|password|varchar(128)|1||0 | 密码
2|last_login|datetime|0||0 | 最后一次登录时间
3|is_superuser|bool|1||0 | 是否是超级用户
4|username|varchar(150)|1||0 | 用户名
5|first_name|varchar(30)|1||0 | 名
6|email|varchar(254)|1||0 | 邮箱
7|is_staff|bool|1||0 | 是否是工作人员
8|is_active|bool|1||0 | 是否是活跃状态
9|date_joined|datetime|1||0 | 加入时间
10|last_name|varchar(150)|1||0 | 姓

### 表名：auth_user_groups
auth_user_groups 表实现了 User 和 Group 之间的多对多关系，即一个用户可以属于多个组，一个组也可以包含多个用户
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1 | 
1|user_id|INTEGER|1||0 | 外键，指向 auth_user 表
2|group_id|INTEGER|1||0 | 外键，指向 auth_group 表


### 表名：auth_user_user_permissions
用于存储用户与权限之间关系的一个中间表。它管理着特定用户所拥有的权限，确保权限与用户之间的关联。这是 Django 默认的认证系统的一部分，帮助实现细粒度的访问控制和授权管理。
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1 
1|user_id|INTEGER|1||0 | 这个字段是 auth_user 表的外键，指向一个具体的用户（User 表）。它表示这个用户所拥有的某个权限。
2|permission_id|INTEGER|1||0 | 这个字段是 auth_permission 表的外键，指向一个具体的权限（Permission 表）。它表示这个用户所拥有的权限

### 表名：django_admin_log
管理员操作日志
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|action_time|datetime|1||0| 记录操作发生的时间
2|object_id|TEXT|0||0|存储操作对象的 ID，这个值是操作对象的主键，通常是一个字符串
3|object_repr|varchar(200)|1||0|该字段保存操作对象的字符串表示（通常是模型实例的字符串表现）
4|change_message|TEXT|1||0| 操作记录的信息
5|content_type_id|INTEGER|0||0|外键，指向 django_content_type 表，表示该操作所属的模型类型。
6|user_id|INTEGER|1||0| 外键，指向 auth_user 表，表示执行该操作的用户
7|action_flag|smallint unsigned|1||0| 操作类型标志。Django 使用一组常量来表示不同类型的操作：


### 表名：django_content_type 
用于存储所有已注册模型的信息 

|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|app_label|varchar(100)|1||0| 存储模型所在的应用的标签（即应用的名称）。例如，如果模型 Article 位于应用 blog 中，那么 app_label 为 blog
2|model|varchar(100)|1||0|存储模型的名称（小写形式）。例如，Article 模型的名称会存储为 article。


### 表名：django_migrations
用于记录数据库迁移状态的表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1 |
1|app|varchar(255)|1||0 | 存储迁移所属的应用的名称（例如 auth、blog）
2|name|varchar(255)|1||0 | 存储迁移的名称，即迁移文件的文件名，不包括扩展名（例如 0001_initial、0002_auto_20240401_1234）
3|applied|datetime|1||0 | 记录迁移应用的时间戳，即该迁移被应用到数据库的时间

### 表名：django_session
一个用于存储用户会话（session）信息的表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|session_key|varchar(40)|1||1
1|session_data|TEXT|1||0|存储会话数据的字段，通常以序列化的形式存储字典或其他数据。Django 会把会话数据序列化为字符串存储在这里
2|expire_date|datetime|1||0 | 记录会话过期的时间。会话过期后，Django 会自动清理该会话的数据。默认情况下，会话会在用户的浏览器关闭时过期，除非设置了其他过期时间


### 表名：facility_facility
设备表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1 |
1|version|varchar(100)|1||0 | 设备型号
2|facility_name|varchar(100)|1||0 | 设备名称
3|price|bigint|1||0 | 价格
4|buy_time|date|1||0 | 购买时间
5|buyer_id|INTEGER|1||0 | 购买人id

### 表名：facility_maintain
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|last_time|date|1||0| 保养时间
2|complmentary|TEXT|1||0| 补充信息
3|facility_id_id|INTEGER|1||0| 设备ID
4|staff_name_id|INTEGER|1||0|　保养员


### 表名：facility_repair
设备报修表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|repair_staff_name_id|INTEGER|0||0| 维修人
2|repair_time|date|0||0| 维修时间
3|facility_id_id|INTEGER|1||0| 设备ID 
4|baoxiu_complementary|varchar(200)|0||0| 报修描述
5|baoxiu_staff_name_id|INTEGER|0||0|报修人
6|baoxiu_time|date|0||0|报修时间
7|baoxiu_staff_tel|varchar(11)|0||0|报修人电话



### 表名：notice_notice
公告表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|title|varchar(100)|1||0 | 标题
2|content|TEXT|1||0 | 内容
3|created_time|date|1||0| 创建时间
4|author_id|INTEGER|0||0| 创建人ID 

### 表名：orders_orders
订单信息表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1 |
1|order_client|varchar(100)|1||0 |客户名称
2|order_time|date|1||0 | 订货时间
3|order_end|date|1||0| 交货时间
4|order_price|INTEGER|1||0 | 单价
5|order_number|INTEGER|1||0 | 数量
6|order_name_id|INTEGER|1||0 | 产品ID 
7|order_total_price|INTEGER|1||0| 订单总价
8|order_supplement|TEXT|0||0 | 补充信息

### 表名：user_attendance
出勤表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|current_time|date|1||0| 日期
2|flag_leave|bool|1||0| 请假
3|flag_business|bool|1||0| 出差
4|start_time|datetime|1||0| 上班时间
5|end_time|datetime|1||0|下班时间
6|staff_name_id|INTEGER|1||0|姓名
7|supplement|varchar(100)|0||0|补充信息

### 表名：user_position
职位
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1
1|position|varchar(100)|1||0|职位名称

### 表名：user_profile
用户信息表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1
1|staff_gender|varchar(10)|1||0|性别
2|staff_age|integer unsigned|1||0|年龄
3|staff_home|varchar(100)|1||0|籍贯
4|staff_nationality|varchar(20)|1||0|民族
5|staff_tel|bigint|1||0|电话
6|start_time|date|1||0|入职时间
7|id_card|varchar(20)|1||0|身份证
8|staff_type|varchar(100)|0||0|职位
9|salary_pre_hour|INTEGER|1||0|时薪
10|user_id|INTEGER|1||0|用户id
11|avatar|varchar(100)|0||0|用户头像


### 表名：user_salary
员工薪资
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|current_time|date|1||0|时间
2|attend_days|INTEGER|1||0|出勤
3|leave_days|INTEGER|1||0|请假
4|absent_days|INTEGER|1||0|旷班
5|business_days|INTEGER|1||0|出差
6|late_days|INTEGER|1||0|迟到
7|overtime|INTEGER|1||0|加班时长
8|base_salary|INTEGER|1||0|基础工资
9|overtime_salary|INTEGER|1||0|加班工资
10|kouchu|INTEGER|1||0|应扣
11|allowance|INTEGER|1||0|补贴
12|should_pay|INTEGER|1||0|应发
13|actual_pay|INTEGER|1||0| 实发
14|staff_name_id|INTEGER|1||0|姓名
15|zaotui_days|INTEGER|1||0|早退
16|tax|INTEGER|1||0|个人所得税

### 表名：warehouse_goods
商品表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1
1|good_name|varchar(100)|1||0|商品名称

### 表名：warehouse_producediary
生产日志
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|current_time|date|1||0|日期
2|staff_name_id|INTEGER|1||0|员工
3|product_name_id|INTEGER|1||0|产品ID　
4|today_done_num|INTEGER|1||0|　今日产量
5|qualified_num|INTEGER|1||0|　合格量
6|facility_id_id|INTEGER|1||0|设备ID

### 表名：warehouse_product
产品表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|product_name|varchar(100)|1||0| 产品名

### 表名：warehouse_purchaselist
采购单
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|good_name|varchar(100)|1||0| 品名
2|good_version|varchar(100)|1||0 | 型号
3|good_num|INTEGER|1||0 | 数量
4|apply_date|date|1||0 | 申请日期
5|sanction_date|date|0||0 | 批准日期
6|price|bigint|0||0| 价格
7|buyer_date|date|0||0| 采购日期
8|apply_staff_name_id|INTEGER|0||0 | 申请人
9|buyer_name_id|INTEGER|0||0|采购员
10|sanction_staff_name_id|INTEGER|0||0 | 批准人
11|total_price|bigint|0||0| 总价

### 表名：warehouse_warehouse
仓库信息
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1 |
1|current_time|date|1||0 | 日期
2|number|INTEGER|0||0 |数量
3|product_name_id|INTEGER|0||0|产品类型
4|unit|varchar(10)|0||0|单位

### 表名：warehouse_warehousesource
仓库信息表
|cid|name|type|notnull|dflt_value|	pk| meaning| 
|-----|------|--------|-----|----|----|---|
0|id|INTEGER|1||1|
1|current_time|date|1||0|日期
2|number|INTEGER|0||0| 数量
3|unit|varchar(10)|0||0| 单位
4|source_name_id|INTEGER|0||0| 原料类型


## 项目架构
**项目的架构、主要运用的技术、程序的运行逻辑（前、后端和数据库如何交互）**
my_project/
├── my_project/           # 主项目目录，包含项目的配置文件
│   ├── __init__.py       # 项目初始化文件
│   ├── settings.py       # 项目的设置文件
│   ├── urls.py           # 项目的 URL 配置文件
│   ├── asgi.py           # ASGI 配置文件（异步支持）
│   └── wsgi.py           # WSGI 配置文件（传统同步支持）
├── my_app/               # 一个 Django 应用目录，包含与某个功能模块相关的文件
│   ├── __init__.py
│   ├── admin.py          # 管理后台配置
│   ├── apps.py           # 应用的配置文件
│   ├── models.py         # 数据库模型文件
│   ├── views.py          # 视图函数文件
│   ├── templates/        # 存放应用模板的目录
│   ├── static/           # 存放静态文件（如 CSS, JS, 图片）的目录
│   ├── migrations/       # 数据库迁移文件目录
│   ├── tests.py          # 测试代码
│   └── urls.py           # 应用的 URL 配置文件
├── manage.py             # Django 的命令行工具文件
└── db.sqlite3            # 数据库文件（如果使用 SQLite）




## 
**把项目代码块文件名字列出，说明这是哪个功能的代码文件**


## 
**一些特定功能的限制如何实现，例如登录模块，如何实现区分管理员和普通员工**