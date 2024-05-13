import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import desc, and_, or_, text, literal

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import BigInteger, Column, DateTime, Enum, Float, Integer, String, Text, text, Date
from sqlalchemy.dialects.mysql import MEDIUMTEXT, TINYINT, INTEGER
from sqlalchemy.types import TypeDecorator

# engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/demo?charset=utf8', echo=True)
engine = create_engine('mysql+pymysql://root:tstack_monitor@192.168.134.106:3306/cloud?charset=utf8')

Base = declarative_base()

# 创建mysql操作对象
Session = sessionmaker(bind=engine)
session = Session()
model_query = session.query


class AlarmUserPolicy(Base):
    __tablename__ = 'alarm_user_policy_v2'

    policy_id = Column(String(50), primary_key=True)
    name = Column(String(1024), nullable=False)
    resource_selector = Column(String(2048), nullable=False)
    alarm_type = Column(String(50), nullable=False)
    alarm_level = Column(Enum(u'1级', u'2级', u'3级', u'4级'), nullable=False)
    alarm_resource_category_code = Column(String(50), nullable=False)
    description = Column(String(1024))
    enable = Column(TINYINT(4), nullable=False)
    composite_operator = Column(Enum(u'and', u'or'), nullable=False)
    time_constraints = Column(String(2048))
    ok_actions = Column(String(2048))
    alarm_actions = Column(String(2048))
    insufficient_data_actions = Column(String(2048))
    repeat_actions = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    created_by = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(50))
    deleted_at = Column(DateTime)
    deleted_by = Column(String(50))
    deleted = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    select_mode = Column(String(50))
    notice_type = Column(String(50))


class AlarmUserPolicyResourceV2(Base):
    __tablename__ = 'alarm_user_policy_resource_v2'

    id = Column(Integer, primary_key=True)
    policy_id = Column(String(50), nullable=False)
    field = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    value = Column(String(50), nullable=False)
    op = Column(String(50), nullable=False)
    dept_id = Column(Integer, default=0)


class object_demo(object):

    def get_alarm_user_policies_by_paging(self, page_index=0, page_size=30):
        page_index = int(page_index) if page_size else 0
        page_size = int(page_size) if page_size else 30

        query = model_query(AlarmUserPolicy)

        query = query.filter(AlarmUserPolicy.deleted == 0)
        query = query.order_by(desc(AlarmUserPolicy.created_at))

        total = query.count()
        results = query.offset(page_index * page_size).limit(page_size).all()

        policy_id_list = []
        for res in results:
            policy_id_list.append(res.policy_id)
        resource_list = self.get_resource_by_policy_id_list(policy_id_list=policy_id_list)

        if len(resource_list) > 0:

            for i, res in results:
                resources = []
                for resource in resource_list:
                    if resource.policy_id == res.policy_id:
                        resources.append(resource)
                results[i].resource_selector = resources

        return results, total


    def get_resource_by_policy_id(self, policy_id):
        return model_query(AlarmUserPolicyResourceV2).filter(
            AlarmUserPolicyResourceV2.policy_id == policy_id).all()

    def get_resource_by_policy_id_list(self, policy_id_list):
        return model_query(AlarmUserPolicyResourceV2).filter(
            AlarmUserPolicyResourceV2.policy_id.in_(policy_id_list)).all()

policy_id = "17EB7AC4-2009-4F84-9644-F3562CE2E988"
ob = object_demo()
resource_list = ob.get_resource_by_policy_id(policy_id=policy_id)

results, total = ob.get_alarm_user_policies_by_paging()

# for i, res in enumerate(results):
#     # print(i, res.policy_id)
#     results[i].resource_selector = resource_list
#
# print(results[0])

# page_index = 0
# page_size = 30
# page_index = int(page_index) if page_size else 0
# page_size = int(page_size) if page_size else 30
# query = session.query(AlarmUserPolicy)
#
# query = query.filter(AlarmUserPolicy.deleted == 0)
# query = query.order_by(desc(AlarmUserPolicy.created_at))
#
# total = query.count()
# results = query.offset(page_index * page_size).limit(page_size).all()
#
# print(total)
