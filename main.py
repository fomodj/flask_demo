## 实现 api 并且实验 api的get post， 以及它的request里的Param query body
## 数据库实例的创建
## 利用工厂模式去创建flask这个实例

## https://dormousehole.readthedocs.io/en/latest/tutorial/database.html
## 用sqlite不需要你去搭建另外的数据库服务器

'''
启动
$env:FLASK_APP='main.py'
flask run
'''

from flask import Flask
from flask import request

app = Flask(__name__)

## 工厂模式是一种很常用的用于创建对象的设计模式

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/name',methods=['GET', 'POST'])
def get_name():
    if request.method == 'POST':
        return 'Fomodj from POST'
    else:
        return 'Fomodj from GET'

@app.route('/fans')
def get_fans():
    return '10000'

# 用户资料endpoint
@app.route('/userProfile',methods=['GET', 'POST'])
def get_profile():
    if request.method == 'GET':
        name = request.args.get('name', '')
        print(name)
        if (name == 'Fomodj'):
            return dict(name='Fomodj from GET',fans=10000)
        else:
            return dict(name='bushi Fomodj from GET',fans=1000000)
    elif request.method == 'POST':
        print(request.form)
        print(request.data)
        print(request.json)
        name = request.json.get('name')
        if (name == 'Fomodj'):
            return dict(name='Fomodj from POST',fans=10000)
        else:
            return dict(name='bushi Fomodj from POST',fans=1000000)
        return '1'