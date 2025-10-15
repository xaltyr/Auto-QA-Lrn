from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    result = browser.find_element(By.CSS_SELECTOR, "#answer")
    result.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "[value = 'robots']")
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
