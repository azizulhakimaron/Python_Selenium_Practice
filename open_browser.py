from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="F:\chromedriver_win32")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.PARTIAL_LINK_TEXT,"Selenium Tutorial").click()
total=driver.find_elements(By.TAG_NAME,"a")
print(len(total))
print("Following are the link present in the webpage")
for totals in total:
    print(totals.text)
driver.close()