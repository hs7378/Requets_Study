# coding=utf-8
import requests
import re
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
url = 'http://www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh'
r =  requests.get(url,headers = headers)
print (r.status_code)
html = r.text
title = re.search('<title>(.*?)</title>',html,re.S)

print (title.group(1))
data = re.search(u'持股:(.*?)',html)
print (data)