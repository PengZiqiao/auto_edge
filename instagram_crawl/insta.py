from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import requests

def save_img(url, filename):
    r = requests.get(url)
    p = Path(f'./{PROFILE}/{filename}')
    p.write_bytes(r.content)

PROFILE = 'kie0087'
STEP = 12
start = 0

driver = webdriver.Edge()
driver.get(f"https://imgsed.com/{PROFILE}/")
input("Ready to go!")


while True:
    driver.execute_script('window.scrollTo (0,document.body.scrollHeight)')

    links = driver.find_elements(By.XPATH, "//a[@class='download']")
    for i, link in enumerate(links[start:start + STEP]):
        url = link.get_attribute('href')
        
        try:
            save_img(url, f'{start}_{i}.jpg')
        except Exception as e:
            continue

    start += STEP