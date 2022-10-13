'''
Created on 2022年8月6日

@author: Quinn
'''
#蝦皮爬蟲測試

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://shopee.tw/JTLEGEND-2022-2020-iPad-Air-5-4-10.9%E5%90%8B-Ness%E7%9B%B8%E6%A9%9F%E5%BF%AB%E5%8F%96%E6%8A%98%E7%96%8A%E9%98%B2%E6%BD%91%E6%B0%B4%E5%B8%83%E7%B4%8B%E7%9A%AE%E5%A5%97_%E5%AE%98%E6%97%97%E5%BA%97-i.6317752.15214214920")
time.sleep(2)
chrome.find_element("xpath","//*[@id='main']/div/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[2]").click()#卡其
chrome.find_element("xpath","//button[text()='直接購買']").click()#直接購買
#chrome.get("https://shopee.tw/buyer/login?is_from_login=true&next=https%3A%2F%2Fshopee.tw%2F%3Fis_from_login%3Dtrue")

time.sleep(1)
chrome.find_element("name","loginKey").send_keys('xxx') #輸入帳號
chrome.find_element("name","password").send_keys('xxx')#輸入密碼
time.sleep(1)
chrome.find_element("xpath","//button[text()='登入']").click()#登入
#chrome.find_element("tagName","登入").click()#登入
#chrome.find_element("css_selector","div[class='yXry6s'] button[class='wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1']").click()#登入

time.sleep(4.5)
chrome.find_element("xpath","//*[@id='main']/div/div[2]/div/div/div/div[1]/div/div[2]/div/button/div[2]").click()#使用連結驗證

time.sleep(10)

# WIDTH = 640
# HEIGHT = 1280
# PIXEL_RATIO = 3.0
# UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
#
# mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
# moptions = webdriver.ChromeOptions()
# moptions.add_experimental_option('mobileEmulation', mobileEmulation)
#driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=moptions)
#driver.get('https://shopee.tw/jean441696?tab=3')




