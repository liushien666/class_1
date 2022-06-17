from linebot import LineBotApi
from linebot.models import TextSendMessage


line_bot_api = LineBotApi('y+lbnel/fNPhyAKv64A4JGWK6vgwpxG2TEfwjXDrUx9AASKSpo8EJ/av+zcBq8EJ59hAuPKKCkCw8+kmMNsgW2Cxr7LmzQ2iE5cR0prvkXVC3jY3GDkHxEVjqBhwMHdhAhTyPslPKKoiXEyjCJZu0wdB04t89/1O/w1cDnyilFU=')
UserID = "U4fb40488b88ed616ee02bc52d88403ee"

import requests
from bs4 import BeautifulSoup


respond = requests.get("https://movies.yahoo.com.tw/movie_thisweek.html")
soup = BeautifulSoup(respond.text,"html.parser")
divs_1 = soup.find_all("div",class_="release_movie_name")
divs_2 = soup.find_all('div',class_="release_btn color_btnbox")


amount = 0

#名稱
for index,each_div in enumerate(divs_1):
    a = each_div.find_all('a')
    
    movieName = a.text

#預告片超連結
for index,each_div in enumerate(divs_2):
    a = soup.find('a',class_="btn_s`_vedio gabtn")
    
    trailerLink = a.url
    

text_message = TextSendMessage(text=movieName)

message = [text_message]
line_bot_api.push_message(UserID,message)