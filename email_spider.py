#-*-coding:utf-8-*-
import re
import requests
import sys
reload(sys)
html1 = requests.get('http://web.xidian.edu.cn/')
html1.encoding = 'utf-8'
#print html1.text

xy_html = re.search(u'<div class="left_title">按院系查找</div>(.*?)<div class="left_title">按姓氏首字母查找</div>',html1.text,re.S).group(1) #编码转换
#xy_html = re.findall('title="(.*?)</a>',html1.text,re.S)
#print xy_html
f1 = open(u'1.txt','w')
f2 = open(u'2.txt','w')
xy_url = re.findall('<a href="(.*?)" title',xy_html,re.S)
for per_xy_url in xy_url:
    temp_xy_url = 'http://web.xidian.edu.cn/' + per_xy_url
    #print temp_url
    html2 = requests.get(temp_xy_url)
    html2.encoding = 'utf-8'
    #print html2.text
    t_html = re.search(u'教师主页\(按字母排列\)</div>(.*?)</ul>',html2.text,re.S).group(1)
    #print t_html
    t_url = re.findall('<a href="(.*?)" title',t_html,re.S)
    for per_t_url in t_url:
        temp_t_url = 'http://web.xidian.edu.cn' + per_t_url
        #print temp_t_url
        html3 = requests.get(temp_t_url)
        html3.encoding = 'utf-8'
        email = re.search(u'电子邮箱：(.*?)@xidian.edu.cn',html3.text,re.S)
        if email :
            temp_email = email.group(1) + '@xidian.edu.cn\n'
            f1.write(temp_email.encode('utf-8'))
        else :
            email = re.search(u'电子邮箱：(.*?)@mail.xidian.edu.cn',html3.text,re.S)
            if email :
                temp_email = email.group(1) + '@mail.xidian.edu.cn\n'
                f2.write(temp_email.encode('utf-8'))
f1.close()
f2.close()
