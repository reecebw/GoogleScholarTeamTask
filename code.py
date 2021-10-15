import scholarly
import requests
import random
import re

useragents = []
useragentfile = open('useragents.txt')
for line in useragentfile:
    useragents.append(line.strip("\n"))
useragentfile.close()
with open('keywords.txt') as f:
    for line in f:
        word = line.replace("\n", "").replace(' ', '+')
        print(word)
        url = "https://scholar.google.com/scholar?start=1&q=%22" + word + '%22&hl=en&as_sdt=0,36&as_ylo=1980&as_yhi=2020'
        session=requests.session()
        header = {'User-Agent' : random.choice(useragents)}
        html = session.get(url, headers = header).text
        print(html)
        index = html.index('gs_ab_mdw">About') #18
        subHtml = html[index::]
        count = re.findall('[0-9,]+',subHtml)[0]
        print(count)