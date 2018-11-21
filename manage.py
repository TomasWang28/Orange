from flask_script import Manager, Server
from livereload import Server as Live_Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from app.modules import User, Role, generate_password_hash
import time

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver",
                    Server(host="127.0.0.1", port=5005, use_debugger=True))


# 启动监控服务
@manager.command
def dev():
    live_server = Live_Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False, port=5000)


@manager.command
def create_db():
    """
    create related  tables
    """
    db.create_all()
    a = User.query.all()
    print(a)


@manager.command
def create_admin():
    role = Role(id=1, role_name='administrator')
    admin = User(id=1, user_name='tomas',
                 user_email='18222273318@163.com',
                 password_hash=generate_password_hash('950428'),
                 created_time=time.strftime("%Y-%m-%d %H:%M:%S",
                                            time.localtime()), role_id=1)

    db.session.add_all([role, admin])
    db.session.commit()  # This is needed to write the changes to database
    print("Default admin user, username:  tomas   password: 950428 ")


# db.create_all()
if __name__ == '__main__':
    manager.run()
    # dev()
