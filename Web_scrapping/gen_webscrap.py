# Here we have scarapped out the title of the page

import requests, bs4
res = requests.get('https://www.google.com')
# result = res.text
# print(result)
soup = bs4.BeautifulSoup(res.text,'lxml')

hi = soup.select('title')
# print(hi)
Title = hi[0].getText()
print(Title)
