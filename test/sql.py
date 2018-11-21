from main import *
import sqlite3
from os import path

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# basedir = path.abspath(path.dirname(__file__))
# DB_URI = 'sqlite:///' + path.join(basedir, 'data.sqlite')
# engine = create_engine(DB_URI)
# Base = declarative_base(engine)
# session = sessionmaker(engine)()
# data=session.query(User.username,User.password).first()[0]
data = User.query.filter_by(username='admin').first()
print(data)

conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
rows = cursor.fetchall()
print(rows[0][0])
print(rows[0][1])
print(rows[0][2])
# users = []
# for r in rows:
#     user = User(r[0],r[1])
#     users.append(user)
conn.commit()
cursor.close()
conn.close()
