from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    price_ready = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element(
        (By.ID, "price"),
        "100"
        )
    )

    if price_ready:
        button = browser.find_element(By.ID,"book")
        button.click()

    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    value = browser.find_element(By.ID, "input_value").text
    answer.send_keys(calc(value))
    
    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()
    
finally:
    
     time.sleep(10)
     browser.quit()
    
    
