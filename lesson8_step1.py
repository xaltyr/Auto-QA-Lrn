from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    answer = str(int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    

finally:
    time.sleep(10)
    browser.quit()
