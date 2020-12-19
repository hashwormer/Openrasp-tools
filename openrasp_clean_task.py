#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author:Darkpot

import requests
import json
import re

def reqWebSite():
    try:
        
        #请求参数头设置，dev测试。prod生产
        url = 'http://YOUR_DOMAIN/v1/iast'
        url_dev_host = 'http://YOUR_DOMAIN/v1/api/rasp/delete'
        url_prod_host = 'http://YOUR_DOMAIN/v1/api/rasp/delete'
        params_dev_host = {"app_id":"YOUR_APPID","expire_time":7200}
        params_prod_host = {"app_id":"YOUR_APPID","expire_time":7200}
        params = {"order":"getAllTasks","data":{"page":1,"app_id":"YOUR_APPID"}}
        headers = {'Content-Type': 'application/json','X-OpenRASP-Token':'YOUR_TOKEN'}
        headers_prod_host = {'Content-Type': 'application/json','X-OpenRASP-Token':'YOUR_TOKEN'}
       
        #请求openrasp后台接口，清除离线主机
        req_dev_host = requests.post(url_dev_host,json=params_dev_host,headers=headers) 
        req_prod_host = requests.post(url_prod_host,json=params_prod_host,headers=headers_prod_host) 
        #请求openrasp后台接口，清除过期扫描任务
        req = requests.post(url,json=params,headers=headers)
        response = req.text
        a = json.loads(response)
        #pat = re.compile(r'([0-9]{1,3})\.') 可只清理ip形式的host
        for i in range(10):
            adict = a["data"]["data"]["result"][i]
            hostname = str(adict["host"])
            port = str(adict["port"])
            #if re.search(pat,hostname):
            params1 ="{\"order\":\"cleanTask\",\"data\":{\"host\":\""+hostname+"\",\"port\":"+port+",\"app_id\":\"YOUR_APPID\"}}"
            params1 = json.loads(params1)
            req1 = requests.post(url,json=params1,headers=headers)


    except:
        print("\n程序执行失败\n")

	
reqWebSite()
	
