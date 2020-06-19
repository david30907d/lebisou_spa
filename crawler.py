from selenium import webdriver
import time

while True:
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.google.com/search?q=%E6%83%85%E6%85%BE%E6%8C%89%E6%91%A9+le+bisou+spa&rlz=1C5CHFA_enTW902TW903&oq=%E6%83%85%E6%85%BE%E6%8C%89%E6%91%A9+le+bisou+spa&aqs=chrome..69i57j69i60l3.723j0j9&sourceid=chrome&ie=UTF-8")
    driver.get("http://lebisouspa.com/")
    time.sleep(120)
    driver.close()