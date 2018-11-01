import requests, bs4
res = requests.get('https://www.learncodeonline.com')
result= res.text
print('result')