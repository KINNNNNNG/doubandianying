'''
Created on 2016年11月1日

@author: K
'''
#encoding UTF-8
import urllib.request
import re
page = 0
m=1
while page<=250:
    x=0
    url1,url2,url3 = "https://movie.douban.com/top250?start=",page,"&filter="
    url = url1+str(url2)+url3
    data = urllib.request.urlopen(url)
    html = str(data.read(),'utf-8')
    p_re = re.compile(r'src="(.+.jpg)"')
    p_url = p_re.findall(html)
    t_re = re.compile(r'img alt="(.*?)"')
    t_txt = t_re.findall(html)
    num_re = re.compile(r'<.+?>([0-9].[0-9])<.+?>')
    num = num_re.findall(html)

    for url in p_url:
        urllib.request.urlretrieve(url,str(m)+" "+t_txt[x]+num[x]+".jpg")
        x+=1
        m+=1
    page+=25
    