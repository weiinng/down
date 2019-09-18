# Django创建项目

```
django -admin startproject 项目名
```

# Django创建超级管理员

- 创建超级管理员使用以下命令：

  python manage.py createsuperuser

- 输入打算使用的登录名：

  username:michaelshu

- 输入Email address：

  Email address:

- 输入密码，需要输入两次，输入密码过程中不显示：

  Password:

  Password(again):

- 当两次密码都相同之后，就会提示superuser创建成功。

  Superuser created successfully

- 修改密码：

  python manage.py changepassword username
  
  运行服务：

```
python manage.py runserver 0.0.0.0:8000
```

在浏览器打开：http://192.168.1.100:8000/admin/



也可以通过超级管理员账号登录后台修改密码：

http://192.168.1.100:8000/admin/auth/user/

# 创建应用层

```
python  manage.py  startapp  应用名字
```

建立应用和项目之间的连续，需要对应用进行注册

```
项目名————>settings.py   --↓
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktes',         <-----以应用的名字进行项目注册
]
```

# 启动项目

简单启动项目 访问 172.0.0.1:8000

```
python manage.py runserver
```

项目指定IP访问  172.0.0.1:8000     本机ip:8000

```
python manage.py runserver 0.0.0.0:8000
```

去Django项目的Sitting中修改——↓

```
ALLOWED_HOSTS = ['*']             //改为型号是指所有IP都可以访问
```

# Django数据库迁移

生成数据库迁移文件

```
python manage.py makemigrations
```

执行迁移生成表

```
python manage.py migrate
```

migrate里面的文件不要删每次迁移形成依赖关系

# 获取到当前的工作目录

```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取到当前的工作目录
```

# 创建与tmplate的连接

```
'DIRS': [os.path.join(BASE_DIR,'template')]，
#需要配置的模板文件夹路径
```

# 修改语言时区

```
LANGUAGE_CODE='zh-hans'
TIME_ZONE='Asia/Shanghai'        //这里面没有背景时间，只有亚洲上海的时间
```

# 数据库

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

# 连接Mysql数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   #指定连接mysql数据库
        'NAME':'bj18',                      #数据库名字//数据库需要手动创建
        'USER':'root',                     #连接mysql的用户名
        'PASSWORD':'mysql',            #用户对应的密码
        'HOST':'localhost',            #指定mysql数据库只当数据库所在IP
        'PORT':3306,                  #用户端口号 默认3306
    }
}
```



# Django保存静态资源

```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
```

# 自定义过滤器

- 注册当前的app/应用层 到 ——> INSTALL_APPS
- 在app项目下面创建templatetags文件夹。
- 在templatetags文件夹下面创建`__init__.py`文件声明当前文件加是一个可以导入的包
- 在templatetags文件夹下创建一个你的.py文件，用来保存对应的过滤器函数
- 导入from django.template import Library
- 需要在这个文件下有一个全局变量名为：register = Library()
- 编写过滤器函数
- 注册函数为真正过滤器
  - @register.filter(name='your_len')
  - register.filter('your_len',get_len)
- 模板页面要想使用自定义过滤器，首先导入过滤器文件：{% load youfilter %}
- {{ var|your_func}}