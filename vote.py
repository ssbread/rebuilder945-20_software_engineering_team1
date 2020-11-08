#!/usr/bin/python3
import mysql.connector
import pymysql
import json,os,sys,getopt,argparse

#投票

# 内部接口：
# 从前端接收的：
# {
#     "user_id":"00001",
#     "user_vote":{
#         "1":"1",
#         "2":"0",
#         "3":"1",
#         ...
#     }
# }
# 返回的：
# {
#     "status":true,
#     "msg":"投票成功"
# }
# {
#     "status":false,
#     "msg":"?"
# }

#模拟数据接收（以字符串形式呈现）
jsonmessage = "{\"user_id\":\"00001\",\"user_vote\":{\"1\":\"1\",\"2\":\"0\",\"3\":\"1\"}}"
print(jsonmessage)
tmp = json.loads(jsonmessage)


mydb = pymysql.connect("localhost","root","","vote_system" )
gcursor = mydb.cursor()

gcursor.execute("SELECT user_group_id FROM account WHERE user_id = %s", tmp['user_id'])
result = gcursor.fetchone()

y=""
for x in tmp['user_vote']:
    if(tmp['user_vote'][x] != "0"):
        if x == result:
            #投票给自己所在组视为无效票
            #模拟回送失败消息
            print("因为投票给自己所属组，投票无效")
            gcursor.close()
            mydb.close()
        else:
            y = y +x
print(y)
try:
    gcursor.execute("UPDATE account SET user_vote = %s WHERE user_id = %s",[ y, tmp['user_id'] ])
    mydb.commit()
    #模拟回送成功消息
    print("投票成功")
except:
    mydb.rollback()
    #模拟回送失败消息
    print("投票失败")

gcursor.close()
mydb.close()