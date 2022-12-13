from test1 import x
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
length=len(x)
number=[]
for i in range(0,length):
    number.append(f"link{i}")
res = {}
for key in number:
    for value in x:
        res[key] = value
        x.remove(value)
        break
print("Resultant dictionary is : " + str(res))
