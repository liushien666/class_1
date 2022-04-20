import requests
from bs4 import BeautifulSoup
import re

respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books/")     #從網址中得到的回覆存於respond
soup = BeautifulSoup(respond.text,"html.parser")            #在BeautifulSoup將網址中得到的回覆的文字用html.parser翻譯成python語言並存於soup中
a_tags = soup.find_all('a',href = re.compile("(\d){10}[?]loc=P_(\d){4}_(\d){3}")) #用soup找所有a開頭接，最後接： 10位數的數字/?loc=p_1000位數字 100位數字  的存在a_tags
for url in a_tags:   #a_tags尋找到的網址中
    if len(url.text)>0:  #當搜尋結果＞0
        with open ("bookUrl.txt","a") as file: #強制開啟一個叫bookUrl.txt的檔案
            file.write(url.text+':'+url['href']) #格式：  書名：超連結
            file.write("\n")    #寫完一項換行