from flask_login import UserMixin,LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.role_name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, index=True)
    user_email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created_time = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.user_name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')     #密码可读

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)            # 生成密码是加密的

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)        # 确认密码是否为True, 比较加密密码 和 明文密码


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


