from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

df = pd.read_csv('data.txt', sep=' ', dtype=str)
driver = webdriver.Edge()

# 登录
driver.get("http://158.1.233.17:18007/AUSPManager/#/Manager/manageUser")
sleep(1)
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary']").click()
sleep(1)
driver.find_element(By.ID, "userCode").send_keys('YOUR USERNAME')
driver.find_element(By.ID, "password").send_keys('YOUR PASSWORD')
driver.find_element(By.XPATH, "/html/body/section[1]/div[2]/div[1]/div/div[2]/form/a").click()
input("Ready to go!")

# 循环新建用户
driver.get("http://158.1.233.17:18007/AUSPManager/#/Manager/manageUser")
sleep(2)
for idx, row in df.iterrows():
    # 打开弹窗
    driver.find_element(By.XPATH, "//a[text()='新增用户']").click()
    # 输入工号
    sleep(1)
    driver.find_element(By.XPATH, "//input[@class='form-control fl']").send_keys(row['id'])
    driver.find_element(By.XPATH, "//button[text()='下一步']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='scrollWrap']/section/div[4]/div/div/div[3]/div[1]/button[2]").click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[text()='确定']").click()
    sleep(1)
