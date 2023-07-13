from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep

users = ['5010656', '5010899', '5010795']
driver = webdriver.Edge()

# 登录
driver.get(r"http://158.1.233.17:18013/virgoFed/#/login?redirect=%2FmyPending")
sleep(1)
driver.find_element(By.XPATH, "//button/span[text()='已知晓']/..").click()
sleep(1)
ele =driver.find_element(By.ID, "password")
ele.send_keys('YOUR PASSWORD')

for name in users:
    print(name)
    ele = driver.find_element(By.ID, "auspUserCode")
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(name)


    driver.find_element(By.CLASS_NAME, "loginSubmit").click()
    sleep(1)

    driver.switch_to.frame("changePwd")

    driver.find_element(By.ID, "oriPwd").send_keys('YOUR PASSWORD')
    driver.find_element(By.ID, "newPwd").send_keys('YOUR PASSWORD')
    driver.find_element(By.ID, "checkNewPwd").send_keys('YOUR PASSWORD')
    driver.find_element(By.CLASS_NAME, "btn-submit").click()
    sleep(1)

    driver.switch_to.default_content()
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    sleep(1)
