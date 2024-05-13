# -*- coding: utf-8 -*-
__author__ = 'luointo'

from datetime import datetime
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


class EvacuationBasicCondition(Base):
    __tablename__ = 'evacuation_basic_condition'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    desc = Column(String(255), nullable=False)
    create_by = Column(String(255), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime)
    deleted = Column(TINYINT(2), nullable=False, server_default=text("'0'"))
    deleted_at = Column(DateTime)
    url = Column(String(255))
    method = Column(String(255))
    params = Column(String(255))
    frequency = Column(Integer, default=0)
    time_interval = Column(Integer, default=0)
    inspect_time_interval = Column(Integer, default=0)


class AlarmUserPolicyEvacuationV2(Base):
    __tablename__ = 'alarm_user_policy_evacuation_v2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    evacuation_bc_id = Column(Integer, nullable=False)
    policy_id = Column(String(50), nullable=False)
    frequency = Column(Integer, default=0)
    time_interval = Column(Integer, default=0)
    inspect_time_interval = Column(Integer, default=0)
    enable = Column(TINYINT(2), nullable=False, server_default=text("'0'"))

class AlarmIgnore(Base):
    __tablename__ = 'alarm_ignore'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(40))
    alarm_resource_category_code = Column(String(40))
    alarm_ignores = Column(String(40))
    create_time = Column(DateTime)
    begin_time = Column(DateTime)
    end_time = Column(DateTime)
    policy_id = Column(String(50), nullable=False)
    ignore_type = Column(String(50), nullable=False)
    duration = Column(Integer)

class object_demo(object):
    def get_evacuation_condition_by_policy_id_list(self, policy_id_list):
        query = model_query(AlarmUserPolicyEvacuationV2)
        query = query.filter(AlarmUserPolicyEvacuationV2.policy_id.in_(policy_id_list))
        query = query.join(EvacuationBasicCondition,
                           AlarmUserPolicyEvacuationV2.evacuation_bc_id == EvacuationBasicCondition.id, isouter=True)
        query = query.with_entities(AlarmUserPolicyEvacuationV2.id,
                                    AlarmUserPolicyEvacuationV2.evacuation_bc_id,
                                    AlarmUserPolicyEvacuationV2.policy_id,
                                    AlarmUserPolicyEvacuationV2.frequency,
                                    AlarmUserPolicyEvacuationV2.time_interval,
                                    AlarmUserPolicyEvacuationV2.inspect_time_interval,
                                    AlarmUserPolicyEvacuationV2.enable,
                                    EvacuationBasicCondition.name,
                                    EvacuationBasicCondition.desc,
                                    EvacuationBasicCondition.url,
                                    EvacuationBasicCondition.method,
                                    EvacuationBasicCondition.params)
        query_result = query.first()

        print(dir(query_result))

        print(query_result.count)

        return []

        result_list = []
        bc_id_list = []
        for res in query_result:
            bc_id_list.append(res.evacuation_bc_id)
            result_list.append({
                "id": res.id,
                "policy_id": res.policy_id,
                "name": res.name,
                "desc": res.desc,
                "url": res.url,
                "method": res.method,
                "params": res.params,
                "frequency": res.frequency,
                "time_interval": res.time_interval,
                "inspect_time_interval": res.inspect_time_interval,
                "enable": res.enable,
            })
        query_basic_condition = model_query(EvacuationBasicCondition)
        query_basic_condition = query_basic_condition.filter(EvacuationBasicCondition.id.notin_(bc_id_list))
        query_basic_condition_result = query_basic_condition.all()

        for res in query_basic_condition_result:
            result_list.append({
                "id": res.id,
                "policy_id": "",
                "name": res.name,
                "desc": res.desc,
                "url": res.url,
                "method": res.method,
                "params": res.params,
                "frequency": res.frequency,
                "time_interval": res.time_interval,
                "inspect_time_interval": res.inspect_time_interval,
                "enable": 0,
            })
        return result_list


    def ignore(self, policy_id):
        should_ignore = model_query(AlarmIgnore).filter(AlarmIgnore.policy_id == policy_id,
                                                        AlarmIgnore.end_time > datetime.now()).all()
        if len(should_ignore) > 0:
            return [], 0

        return 112


policy_id = "93EDA5B7-9078-4EEE-8A3E-8E927E09BDBB"
ob = object_demo()

result = ob.ignore(policy_id)
print(result)

# # resource_list = ob.get_evacuation_condition_by_policy_id(policy_id=policy_id)
#
# policy_id_list = [
#     "C38D1B90-4F3A-43F9-A967-B661C040917C"
# ]
# resource_list = ob.get_evacuation_condition_by_policy_id_list(policy_id_list=policy_id_list)
#
# for data in resource_list:
#     print(data)
#
# # print(resource_list)
