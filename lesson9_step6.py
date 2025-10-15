from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    rainbow_button = browser.find_element(By.CSS_SELECTOR, ".trollface")
    rainbow_button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    answer = browser.find_element(By.CSS_SELECTOR, ".form-control")
    answer.send_keys(calc(value))

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit
