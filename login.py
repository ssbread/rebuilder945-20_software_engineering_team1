#!/usr/bin/python3
import mysql.connector
import pymysql
import json,os,sys,getopt,argparse

mydb = pymysql.connect("localhost","root","","vote_system" )

#登录

# 内部接口：
# 从前端接收的：
# {
#     "user_id":"00001",
#     "user_key":"12345"
# }
# 返回的：
# {
#     "status":true,
#     "msg":"登录成功"
# }
# {
#     "status":false,
#     "msg":"?"
# }

#模拟数据接收（以字符串形式呈现）
jsonmessage = "{\"user_id\":\"00001\",\"user_key\":\"00001\"}"
tmp = json.loads(jsonmessage)


while 1:
    mycursor = mydb.cursor()


    UserName = tmp['user_id']
    UserKey = tmp['user_key']
    mycursor.execute("SELECT user_key FROM account WHERE user_id = %s", UserName)
    result = mycursor.fetchone()
    if result[0] == UserKey:
        #模拟回送成功消息
        print("登录成功")
        break
    else:
        #模拟回送失败消息
        print("密码错误")

mycursor.close()
mydb.close()
