# -*- coding:utf-8 -*-
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from mixhelp import crate_app
from mixhelp.extensions import db
from mixhelp.models.problem import Problem_SKU, Problem_SPU
# 创建命令行manager对象
app = crate_app('develop')
manager = Manager(app)


# 创建Migrate
Migrate(app, db)


server = Server(host='0.0.0.0', port=5000)

# 给manager添加命令
manager.add_command('server', server)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()