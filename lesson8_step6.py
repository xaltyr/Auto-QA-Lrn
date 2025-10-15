from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element(By.ID, "input_value").text

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(value))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    browser.execute_script("window.scrollBy(0, 100);")

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
