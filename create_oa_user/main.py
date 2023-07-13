from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

df = pd.read_csv('data.txt', sep=' ', dtype=str)
driver = webdriver.Edge()


"""
OA操作
"""
# 登录
driver.get("http://158.1.233.14:28991/xcoa/admin/home.jsp")
driver.find_element(By.ID, "account").send_keys('YOUR　ACCOUNT')
driver.find_element(By.ID, "passwd").send_keys('YOUR PASSWORD')
driver.find_element(By.ID, "login").click()
input("Ready to go!")

# 循环新建用户
for idx, row in df.iterrows():
    # 打开弹窗
    print(row['id'], row['name'], row['dept'], sep='|')
    driver.find_element(By.XPATH, "//button[@cmd='newUser']").click()
    # 输入工号、密码、姓名
    
    sleep(1)
    driver.find_element(By.ID, "account").send_keys(row['id'])
    driver.find_element(By.ID, "password").send_keys("YOUR PASSWORD")
    driver.find_element(By.ID, "password2").send_keys("YOUR PASSWORD")
    driver.find_element(By.ID, "name").send_keys(row['name'])
    # 选择职务
    driver.find_element(By.ID, "level").click()
    dropdown = driver.find_element(By.ID, "level")
    dropdown.find_element(By.XPATH, "//option[@value='USER']").click()
    # 选择所在部门
    driver.find_element(By.XPATH, "//input[@value='组织机构']").click()
    sleep(0.5)
    driver.find_element(By.ID, "dropDownTree_parentId_2_switch").click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, row['dept']).click()
    # 提交
    driver.find_element(By.XPATH, "//button[text()='确定']").click()
    sleep(3)
