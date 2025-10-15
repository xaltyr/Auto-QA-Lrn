from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    blue_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    blue_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    answer = browser.find_element(By.CSS_SELECTOR, ".form-control")
    answer.send_keys(calc(value))

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit
