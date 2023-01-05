# coding:UTF-8
import random
import threading
from threading import  Timer
import time
import re
import requests
import os.path
from selenium import webdriver
import tool



# 输入知乎文章网址
homeUrl = input("请输入知乎文章网址")
# homeUrl = "https://www.zhihu.com/question/389411983/answer/1859034765"

downFolder = input("请输入目标文件夹")

# 此处使用selenium而不是requests来抓取数据，因为知乎是动态加载的
option = webdriver.ChromeOptions()
option.add_argument(r'user-data-dir=C:\Users\li\AppData\Local\Google\Chrome\User Data')
# option.add_argument("blink-settings=imagesEnabled=false")
driver = webdriver.Chrome(options=option)
driver.get(homeUrl)

#执行一段js代码，将滚动条滑到底部
js = '''var h = document.documentElement.scrollHeight || document.body.scrollHeight;
  i=1
  time = setInterval(function(){
    console.log(parseInt(h*(i/10)))
    window.scrollTo(0,parseInt(h*(i/10)))
    i++;
    if(i==11){
      clearInterval(time)
    }
  },1000)'''
driver.execute_script(js)

#selenium加载较慢，等待10秒
time.sleep(10)
text = driver.page_source.lower()
print(text)
# 正则图片链接
# https://pica.zhimg.com/80/v2-9e04af318e6988c5f94c2aa3bcee3935_1440w.jpg?source=1940ef5c
# https://pic3.zhimg.com/80/v2-578fd6ba471727c51ff5fdbd4b917c62_1440w.jpg?source=1940ef5c
ree = 'https://pic.\.zhimg\.com/80/v2-.{30,100}jpg?'
imgList = re.findall(ree, text)
print("图片张数："+str(len(imgList)))

#分别下载每张图片，根据requests
num = 0
for imgUrl in imgList:
    time.sleep(1)
    num += 1
    # 调用tool文件中的二进制文件下载方法
    tool.requests_download_wb(imgUrl, downFolder, str(num) + ".jpg",0)
    print(imgUrl)
    print("第" + str(num) + "张图片已经完成")
    if(num == len(imgUrl)):
        print("下载全部完成")
