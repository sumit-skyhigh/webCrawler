import requests
from collections import Counter
import nltk, re, pprint
from bs4 import BeautifulSoup
from nltk import word_tokenize
targetSite = 'http://www.prothom-alo.com/'
# r = requests.get('http://www.prothom-alo.com/sports/article/1101340/%E0%A6%A4%E0%A6%BE%E0%A6%AE%E0%A6%BF%E0%A6%AE%E0%A7%87%E0%A6%B0-%E0%A6%A6%E0%A6%BE%E0%A6%B0%E0%A7%81%E0%A6%A3-%E0%A6%95%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%9A%E0%A7%87-%E2%80%8C%E2%80%98%E0%A6%A1%E0%A6%BE%E0%A6%AC%E0%A6%B2%E2%80%99-%E0%A6%B9%E0%A6%B2%E0%A7%8B-%E0%A6%A8%E0%A6%BE-%E0%A6%AE%E0%A7%87%E0%A6%A8%E0%A7%8D%E0%A6%A1%E0%A6%BF%E0%A6%B8%E0%A7%87%E0%A6%B0')
req = requests.get(targetSite)

soup = BeautifulSoup(req.text, 'html.parser')
links = soup.find_all('a')
a = []
for art in links:  # iterate over loop [above sections]
    if (art['href'].find('https') == -1 and art['href'].find('http') == -1 and art['href'].find('javascript') == -1):
        if (len(art['href']) > 50):
            break
        else:
            a.append(art['href'])

a.remove('/')
count = 1
for item in a[2:2]:
    req = requests.get('http://www.prothom-alo.com/' + item)
    soup = BeautifulSoup(req.text, 'html.parser')
    links = soup.find_all('a')

articles = []
for art in links:  # iterate over loop [above sections]
    if (art['href'].find('article') >= 0 and art['href'].find(a[2]) >= 0):
        articles.append(art['href'])
        # print(art['href'])
print('total'+str(len(articles)))
# articles = list(set(articles))
print('total'+str(len(articles)))

sentence = ''

for item in articles[:20]:
    artReq = requests.get(targetSite + item)
    soup = BeautifulSoup(artReq.text, 'html.parser')
    print(soup.title)
    sentence += " " + str(soup.title.contents[0].strip())
words = re.findall(r'\w+', sentence)
two_words = [' '.join(ws) for ws in zip(words, words[1:])]
wordscount = {w:f for w, f in Counter(two_words).most_common() if f > 1}
print(wordscount)
# titles = titles.split(' ')
# token = word_tokenize(titles)
# text = nltk.Text(token)

# print(text[1:10])
# if (art['href'].find('https') == -1 and art['href'].find('http') == -1 and art['href'].find('javascript') == -1):
#     if (art['href'].find(item) == 0) and art['href'].find('article'):
#         articles.append(art['href'])
#         print(art['href'])
#
# file = open(item+".txt","wb")
# count=count+1
# # soup = BeautifulSoup(r.text,'html.parser')
# file.write(r.text.encode('utf8'))
# print(r.text)
