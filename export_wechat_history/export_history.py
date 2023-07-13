from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
from time import sleep

driver = webdriver.Edge()
driver.get("https://work.weixin.qq.com/wework_admin/frame?version=4.1.0.6011&platform=win#index")
input('ready go~!')


# 定义常用xpath
xpath_submitdate = "//div[contains(@class,'t-range-input__inner-left')]"
xpath_year = "//div[contains(@class, 't-date-picker__header-controller-year')]"
xpath_month = "//div[contains(@class, 't-date-picker__header-controller-month')]"
xpath_first_day = "//td[contains(@class, 't-date-picker__cell--first-day-of-month')]//div"
xpath_end_day = "//td[not(contains(@class, 't-date-picker__cell--disabled'))]"
xpath_button = "//a[contains(text(), '导出记录')]"
xpath_query_result = "//span[@class='approval-list-sum']"


# 选择一个月的日期
year_ = 0
def select_date(year, month, day):
    # 打开日历面板
    driver.find_element(By.XPATH, xpath_submitdate).click()
    sleep(0.5)

    # 当年份不一致时，选择年份
    global year_
    if year != year_:
        year_ = year
        driver.find_element(By.XPATH, xpath_year).click()
        sleep(0.5)
        driver.find_element(By.XPATH, f"{xpath_year}//span[text()='{year}']").click()
        sleep(0.5)

    # 选择月份
    driver.find_element(By.XPATH, xpath_month).click()
    sleep(0.5)
    driver.find_element(By.XPATH, f"{xpath_month}//span[text()='{month}月']").click()
    sleep(0.5)

    # 选择首尾日期
    driver.find_element(By.XPATH, xpath_first_day).click()
    sleep(0.5)
    driver.find_element(By.XPATH, f"{xpath_end_day}//div[text()='{day}']").click()
    sleep(0.5)


# 等待查询数据加载
query_result = driver.find_element(By.XPATH, xpath_query_result).text
def wait_loading():
    print('wait loading...')

    global query_result
    if driver.find_element(By.XPATH, xpath_query_result).text == query_result == '共0条申请记录':
        sleep(1)
    else:
        i=0
        while driver.find_element(By.XPATH, xpath_query_result).text == query_result or i > 15:
            sleep(0.5)
            i+=1

    query_result = driver.find_element(By.XPATH, xpath_query_result).text
    
    print('done!')

def download():
    # 尝试下载
    try:
        driver.find_element(By.XPATH, xpath_button).click()
        print('downloading...')
        sleep(2)

        # 等待下载完成
        WebDriverWait(driver, 30, ).until(EC.presence_of_element_located((By.XPATH, xpath_button)))
        print('done!')
    except:
        print('no results found.')

while True:
    # 定义查询日期范围
    START = input('>>> input start date(yyyy/mm/dd):')
    END = input('>>> input end date(yyyy/mm/dd):')
    date_range = pd.date_range(START, END, freq='M')

    # 走起
    for each in date_range:
        year, month, day = each.year, each.month, each.day
        print(f'>>> {year}-{month}-{1} ~ {year}-{month}-{day}')

        select_date(year, month, day)
        wait_loading()
        download()

        # 减速防跪
        sleep(5)
