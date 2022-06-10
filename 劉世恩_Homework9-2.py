#def functionName()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

chrome = webdriver.Chrome()
chrome.get("https://pic.sogou.com/")
time.sleep(0.5)

def search():
    inputBar = chrome.find_element_by_name("query")
    inputBar.send_keys("puppy")
    inputBar.send_keys(Keys.ENTER)
    time.sleep(0.5)
    chrome.maximize_window()
    time.sleep(0.5)
    for i in range(2):
        chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(2)
    time.sleep(2)
    i=1
    for element in chrome.find_elements_by_class_name('img-layout'):
        img_tag = element.find_element_by_tag_name('img')
        if img_tag:
            img_url = img_tag.get_attribute('src')
            imgRespond = requests.get(img_url)
            with open("image\\"+'puppy'+str(i)+".jpg","bw") as file:
                file.write(imgRespond.content)
        if i ==30:
            break
        i+=1

search()
time.sleep(0.5)
chrome.close()