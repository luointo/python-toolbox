# -*- coding: utf-8 -*-
__author__ = 'luointo'


from selenium import webdriver

url = 'https://www.lagou.com/zhaopin/Java/?labelWords=label'

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")
driver.get(url)
items = driver.find_elements_by_xpath("//ul[@class='item_con_list']/li")
print(len(items))
for item in items:
    title = item.find_element_by_xpath("./div[1]/div[1]/div[1]/a/h3").text
    print(title)
