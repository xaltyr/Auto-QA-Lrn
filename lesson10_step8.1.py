from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # 1. Убрать лишнюю проверку if price_ready
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    # 2. Кнопка будет найдена только после выполнения ожидания
    button = browser.find_element(By.ID, "book")
    button.click()

    # 3. Добавить явное ожидание для появления поля ввода
    answer = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "answer"))
    )
    
    # Скролл к элементу
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    
    # 4. Получить значение и вычислить ответ
    value = browser.find_element(By.ID, "input_value").text
    result = calc(value)
    answer.send_keys(result)
    
    # 5. Нажать кнопку решения
    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()
    
    # 6. Получить результат из alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Результат: {alert_text}")
    alert.accept()
    
finally:
    time.sleep(2)  # 7. Уменьшить время ожидания
    browser.quit()