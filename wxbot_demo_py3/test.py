#!python3
#coding=utf-8

import urllib,requests   
import os,sys,io,json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url = "http://www.tuling123.com/openapi/api"#'http://www.xiaodoubi.com/bot/chat.php'

r = requests.post(url, data={'key':"b8bb8bf591af8b522652fc2aa1e4a03a",'info':"lalala",'userid':"cgddgc"})
print(json.loads((r.text))["text"])

