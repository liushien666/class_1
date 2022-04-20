import re

string = input("請輸入gmail:")    #顯示“請輸入gmail:”並讓使用者輸入gmail
print(re.match("[0-9A-Za-z]+@gmail.com",string)) #判別前半為0~9或A~Z或a~z，並以@gmail.com結尾
print(re.match("\w+@gmail.com",string))          #判別前半為數字字母或底線，並以@gmail.com結尾