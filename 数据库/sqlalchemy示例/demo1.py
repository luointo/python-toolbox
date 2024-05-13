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


class ServerInfoEx2(Base):
    __tablename__ = 'server_info_ex'

    uuid = Column(String(64), primary_key=True)
    name = Column(String(255))
    idc_parent_name = Column(String(255))
    idc_name = Column(String(255))
    idc_id = Column(String(36))
    idc_parent_id = Column(String(36))
    rack_name = Column(String(255))
    asset_id = Column(String(255))
    device_class = Column(String(255))
    ip = Column(String(255))
    owner_asset_id = Column(String(255))
    bsi_id = Column(String(36))
    business_path = Column(String(255))
    pos_code = Column(Integer)
    operator = Column(String(255))
    dept_id = Column(Integer)
    dept_name = Column(String(255))
    status_name = Column(String(255))
    owner_uuid = Column(String(64))
    bak_operator = Column(String(255))
    project_id = Column(String(64))
    project_name = Column(String(128))
    os_name = Column(String(80))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    created_by = Column(String(255))
    updated_by = Column(String(255))
    cmdb_id = Column(String(36))
    wan_ip = Column(String(255))
    lan_ip = Column(String(255))
    business_module_name = Column(String(255))
    business_name = Column(String(255))
    business_raw_name = Column(String(255))
    region_name = Column(String(255))
    region_id = Column(String(36))
    idc_city_id = Column(String(36))
    idc_city_name = Column(String(255))
    category = Column(String(255))
    cpu = Column(Integer)
    ram = Column(Integer)
    host_type = Column(Integer)
    disk_size = Column(Integer)
    machine_type_id = Column(String(36))
    components = Column(String(255))
    purpose = Column(String(255))
    bsi_category = Column(String(255))
    machine_type_name = Column(String(255))
    pos_unit = Column(Integer)


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

        # for data in resource_list:
        #     print(data.name)

        if len(resource_list) > 0:
            for i, res in enumerate(results):
                results[i].rs_list = [x for x in resource_list if x.policy_id == res.policy_id]
        else:
            for i, res in enumerate(results):
                results[i].rs_list = []
        return results, total

    def get_resource_by_policy_id(self, policy_id):
        return model_query(AlarmUserPolicyResourceV2).filter(
            AlarmUserPolicyResourceV2.policy_id == policy_id).all()

    # def get_resource_by_policy_id_list(self, policy_id_list):
    #     return model_query(AlarmUserPolicyResourceV2).filter(
    #         AlarmUserPolicyResourceV2.policy_id.in_(policy_id_list)).all()

    def get_resource_by_policy_id_list(self, policy_id_list):
        query = model_query(AlarmUserPolicyResourceV2)
        query = query.filter(AlarmUserPolicyResourceV2.policy_id.in_(policy_id_list))
        query = query.join(ServerInfoEx2, AlarmUserPolicyResourceV2.value == ServerInfoEx2.uuid, isouter=True)
        query = query.with_entities(AlarmUserPolicyResourceV2.id,
                                    AlarmUserPolicyResourceV2.policy_id,
                                    AlarmUserPolicyResourceV2.field,
                                    AlarmUserPolicyResourceV2.type,
                                    AlarmUserPolicyResourceV2.value,
                                    AlarmUserPolicyResourceV2.op,
                                    AlarmUserPolicyResourceV2.dept_id,
                                    ServerInfoEx2.name,
                                    ServerInfoEx2.dept_name,
                                    ServerInfoEx2.ip)

        return query.all()


policy_id = "0A8A4D46-A3A7-4954-9586-EB6A57EA50B6"
ob = object_demo()
resource_list = ob.get_resource_by_policy_id(policy_id=policy_id)

results, total = ob.get_alarm_user_policies_by_paging()

print(total)
print(results[0].rs_list)

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
