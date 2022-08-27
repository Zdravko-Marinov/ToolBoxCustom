from curses import raw
from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
links = []
flink = []

## make target input
target = "https://github.com/usernam121"
chromeSer = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chromeSer)
driver.get(target)
res = driver.find_elements(By.CLASS_NAME,"repo")


def get_raw(third_page):
    driver.get(third_page)
    raw_button = driver.find_element(By.CLASS_NAME,"js-permalink-replaceable-link")
    raw_button.click()

    htlm = driver.page_source
    htlm = f"{htlm}"

    if("password" in htlm):
        print(f"found password {third_page}")

def loop(next_page):
    a = None

    driver.get(next_page)
    file_name = driver.find_elements(By.CLASS_NAME,"js-navigation-open")

    for a in file_name:
        pass

    if "py" in a.text:
        second_page = f"{next_page}/blob/main/{a.text}"
        get_raw(second_page)
        print(second_page)


for i in res:
    links.append(i.text)

for l in links:
    next_page=f"{target}/{l}"
    flink.append(next_page)
    loop(next_page)

print(flink)

print(links)

driver.quit()