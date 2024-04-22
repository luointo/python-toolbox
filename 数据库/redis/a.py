# -*- coding: utf-8 -*-
__author__ = 'luointo'

# https://www.cnblogs.com/xuchunlin/p/7064860.html

# import redis
# pool = redis.ConnectionPool(host='redis', port=6379, password='')
# r = redis.Redis(connection_pool=pool)
# # r.set('foo', 'bar')
# data = r.hgetall("20210907:6CA3FB4C-372F-5126-95AC-C94B2FE3E4AF:30105")
# print data

import rediscluster

cluster = rediscluster.StrictRedisCluster(startup_nodes=[{'host': 'redis', 'port': '6379'}],
                                          max_connections=500,
                                          password='')

data = cluster.hgetall("20210907:6CA3FB4C-372F-5126-95AC-C94B2FE3E4AF:30105")
print data