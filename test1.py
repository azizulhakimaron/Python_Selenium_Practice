from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.com/s?k=amino+acids&crid=10QX1Y5NF82A&sprefix=amino%2Caps%2C365&ref=nb_sb_ss_ts-doa-p_2_5")

elems = driver.find_elements(By.TAG_NAME,"a")
x=[]
for elem in elems:
    link=elem.get_attribute("href")
    x.append(link)
#print(x)

