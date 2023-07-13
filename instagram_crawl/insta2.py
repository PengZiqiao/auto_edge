from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import requests

def save_img(url, filename):
    r = requests.get(url)
    p = Path(f'./{PROFILE}/{filename}')
    p.write_bytes(r.content)

PROFILE = 'waneella'

driver = webdriver.Edge()
driver.get(f"https://imgsed.com/{PROFILE}/")
input("Ready to go!")


while True:
    driver.execute_script('window.scrollTo (0,document.body.scrollHeight)')
    sleep(2)

    links = driver.find_elements(By.XPATH, "//a[@class='download']")
    print(len(links))

    urls = '\n'.join((link.get_attribute('href') for link in links))
    Path(f'./{PROFILE}.txt').write_text(urls)