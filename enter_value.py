from selenium import webdriver
driver=webdriver.Chrome(executable_path="F:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element("email").send("rrzaron@gmail.com")