from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

target = "https://github.com/usernam121"
chromeSer = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chromeSer)
driver.get(target)
res = driver.find_elements(By.CLASS_NAME,"repo")

links = []
flink = []

def loop(next_page):
    a = None

    driver.get(next_page)
    file_name = driver.find_elements(By.CLASS_NAME,"js-navigation-open")

    for a in file_name:
        pass

    if "py" in a.text:
        print("it works")

        
    time.sleep(2)

for i in res:
    links.append(i.text)

for l in links:
    next_page=f"{target}/{l}"
    flink.append(next_page)
    loop(next_page)

print(flink)

print(links)

driver.quit()