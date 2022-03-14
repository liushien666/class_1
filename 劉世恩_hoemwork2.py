import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books') #get HTML
soup = BeautifulSoup(res.text,'html.parser')                          #過濾HTML   html.parser==>過濾器
divs = soup.find_all("div",class_="type02_bd-a")                      #list

amount = 0
for index,each_div in divs:
    h4 = each_div.find('h4')                #暢銷書排行榜的皆有h4
    if not h4:
        continue
        a = h4.find('a')                   #且為超連結==>書名
        if not a:
            continue
            bookName = a.text
            print('rank'+str(index+1)+': ' +bookName)
            ul = each_div.find('ul')
            lis = ul.find_all('li')
            for each_li in lis:
                strongs = each_li.find_all('strong')
                if strongs:
                    b = strongs[-1].find('b')
                    print('price: '+b.text+'dollars')
                    amount+=1
                    if amount>29:
                        break