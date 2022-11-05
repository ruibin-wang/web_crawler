import urllib.request
import webbrowser as web


import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/?tn=78040160_5_pg&ch=8'
response = requests.get(url).content.decode('utf-8')

title = re.findall(r'<ul>(.*?)</ul>', response, re.S|re.M)

# hot_search = re.findall(r'')


## beautifulsoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

content = requests.get(url, headers=headers).text
soup = BeautifulSoup(content, 'lxml')


# hot_search = soup.find_all(attrs={"class":"s-hotsearch-content"})
hot_search = soup.find_all(attrs={"class":"title-content-title"})

for texts in hot_search:
    print(texts.get_text())


print(response)







