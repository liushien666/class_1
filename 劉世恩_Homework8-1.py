from selenium import webdriver
from selenium.webdriver.common.keys import Ｋeys
import time
chrome = webdriver.Chrome()
chrome.get("https://accounts.google.com/ServiceLogin/signinchooser?hl=zh-TW&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
accountScelect = chrome.find._element_by_class_name("d2laFc")
accountScelect.click()

inputBar = chrome.find_element_by_class_name("whsOndzHQkBf")
inputBar.send_keys("123pAsS45wOrD6789")
time.sleep(0.5)

inputBar.send_keys(Keys.ENTER)