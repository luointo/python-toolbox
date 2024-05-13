# -*- coding: utf-8 -*-
__author__ = 'luointo'

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import desc, and_, or_, text, literal

# engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/demo?charset=utf8', echo=True)
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/demo?charset=utf8')

Base = declarative_base()

# 创建mysql操作对象
Session = sessionmaker(bind=engine)
session = Session()


class User1(Base):
    __tablename__ = 'users1'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # fullname = Column(String(50))
    nickname = Column(String(50))
    begin_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<User1(id='%d', name='%s', , nickname='%s', begin_time='%s', end_time='%s')>" % (
            self.id, self.name,  self.nickname, self.begin_time, self.end_time)


class User2(Base):
    __tablename__ = 'users2'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
    begin_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<User2(name='%s', fullname='%s', nickname='%s', begin_time='%s', end_time='%s')>" % (
            self.name, self.fullname, self.nickname, self.begin_time, self.end_time)


class User3(Base):
    __tablename__ = 'users3'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
    begin_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<User3(name='%s', fullname='%s', nickname='%s', begin_time='%s', end_time='%s')>" % (
            self.name, self.fullname, self.nickname, self.begin_time, self.end_time)




# # 定义初始化数据库函数
# def init_db():
#     Base.metadata.create_all(engine)
#
#
# # 顶固删除数据库函数
# def drop_db():
#     Base.metadata.drop_all(engine)


# drop_db()
# init_db()
#
# d = datetime.datetime.now()
#
# data_list = []
# for n in range(1, 11):
#     begin_time = d + datetime.timedelta(minutes=10*n)
#     end_time = d + datetime.timedelta(minutes=20*n)
#     user1 = User1(id=n, name=f"user1 {n}", fullname=f"fullname{n}", nickname=f"fullname{n}", begin_time=begin_time, end_time=end_time)
#     user2 = User2(id=n+10, name=f"user2 {n}", fullname=f"fullname{n}", nickname=f"fullname{n}", begin_time=begin_time, end_time=end_time)
#     user3 = User3(id=n+20, name=f"user3 {n}", fullname=f"fullname{n}", nickname=f"fullname{n}", begin_time=begin_time, end_time=end_time)
#     data_list.append(user1)
#     data_list.append(user2)
#     data_list.append(user3)
# session.add_all(data_list)
# session.commit()

ed_user = User1(name='a11', nickname='edsnickname', begin_time=datetime.datetime.now(), end_time=datetime.datetime.now())
session.add(ed_user)
session.commit()


# session.add_all({
#     User1(name='a11', fullname='a11', nickname='a11'),
#     User1(name='a12', fullname='a12', nickname='a12'),
#     User2(name='a21', fullname='a21', nickname='a21'),
#     User2(name='a22', fullname='a22', nickname='a22'),
#     User3(name='a31', fullname='a31', nickname='a31'),
#     User3(name='a32', fullname='a32', nickname='a32'),
# })
# session.commit()

# query_active = query_active.order_by(desc(AlarmActive.start_time))

# q1 = session.query(User1)
# # q1 = q1.order_by(text('begin_time desc'))
# q2 = session.query(User2.name.label('name'), User2.fullname.label('fullname'))
# q2 = q2.filter(User2.id > 15)
# # q2 = q2.order_by(desc(User2.begin_time))
# q3 = session.query(User3)
# # q3 = q3.order_by(text('begin_time desc'))
# # q3 = q3.filter(User3.name == "a32")
# # query.offset(page_index * page_size).limit(page_size).all()
# # res = q1.union(q2, q3).offset(2).limit(2).all()
# res = q1.union(q2, q3).all()
# # res = q1.union(q2, q3).order_by(text('begin_time desc'))
# # res = q1.all()

# begin_time = datetime.datetime.strptime('2021-07-24 00:00:44', '%Y-%m-%d %H:%M:%S')
# end_time = datetime.datetime.strptime('2021-07-24 02:30:44', '%Y-%m-%d %H:%M:%S')
#
# q1 = session.query(User1.name.label('name'), User1.begin_time.label('begin_time'), literal('').label('aaa'))
#
# res = q1.all()
#
# for line in res:
#     print(line)
# exit()
#
# q1 = q1.filter(and_(User1.begin_time >= begin_time), User1.end_time <= end_time)
# q2 = session.query(User2.name.label('name'), User2.begin_time.label('begin_time'))
# q2 = q2.filter(User2.name == "user2 4")
# q3 = session.query(User3.name.label('name'), User3.begin_time.label('begin_time'))
#
# q_list = [q2, q3]
#
# print(type(q_list[0]))
#
# # res = q1.union_all(*q_list).order_by(text('begin_time desc'))
# res = q1.union_all(*q_list)
#
# print(str(res))
#
# for line in res:
#     print(line, line.name)

