# This scrap out title of the page and topic tilte

import requests,bs4

res =requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('.mw-headline')
for i in soup.select('.mw-headline'):
    print(i.text)