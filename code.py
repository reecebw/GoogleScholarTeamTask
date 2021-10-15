import scholarly
import requests
import random
import re
from torpy.http.requests import TorRequests
useragents = []
useragentfile = open('useragents.txt')
for line in useragentfile:
    useragents.append(line.strip("\n"))
useragentfile.close()
worddict = {}
with open('keywords.txt') as f:
    for line in f:
        word = line.replace("\n", "").replace(' ', '+')
        print(word)
        yearlyhits = []
        for i in range(40):
            year = 1980 + i
            url = "https://scholar.google.com/scholar?start=1&q=%22" + word + '%22&hl=en&as_sdt=0,36&as_ylo=' + str(year) +'&as_yhi=' + str(year)
            header = {'User-Agent' : random.choice(useragents)}
            with TorRequests() as tor_requests:
                with tor_requests.get_session() as sess:
                    html = sess.get(url, headers = header).text
            #print(html)
            index = html.index('<div id="gs_ab_md"><div class="gs_ab_mdw">') #18
            subHtml = html[index::]
            count = re.findall('[0-9,]+',subHtml)[0]
            yearlyhits.append(count)
            print(year)
            print(count)
        worddict.update({word:yearlyhits})

with open('output.txt') as f:
    f.write(worddict)