from bs4 import BeautifulSoup
import lxml
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
scoup = BeautifulSoup(html,'lxml')
print(scoup.title.string)
# print(scoup.head)
# print(scoup.p)
for link in scoup.find_all('a'):
    print(link.get('href'))
tables = scoup.findAll('table')
tab = tables[2]
for tr in tab.findAll('tr'):
    td = tr.findAll('td')
    print(type(td))
    # print(td[0].getText())
    # for td in tr.findAll('td'):
    #     print(td.getText())
print('SB')