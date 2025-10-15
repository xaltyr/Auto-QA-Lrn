from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
     link = "https://suninjuly.github.io/file_input.html"
     browser = webdriver.Chrome()
     browser.get(link)

     first_name = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
     first_name.send_keys("JoJo")

     last_name = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")                                  
     last_name.send_keys("Bizzare")

     email = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
     email.send_keys("Adventure")

     current_dir = os.path.abspath(os.path.dirname(__file__))
     file_name = "lesson_file.txt"
     file_path = os.path.join(current_dir, file_name)

     element = browser.find_element(By.CSS_SELECTOR, "[name = 'file']")
     element.send_keys(file_path)

     submit = browser.find_element(By.CSS_SELECTOR, ".btn")
     submit.click()

finally:
    time.sleep(10)
    browser.quit
