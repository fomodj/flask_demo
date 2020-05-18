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

import os

from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from . import db
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

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

    return app