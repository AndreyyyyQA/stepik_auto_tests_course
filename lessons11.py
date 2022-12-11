from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try: 

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book = browser.find_element(By.ID, "book")
    book.click()
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    option1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    option1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    button.click()

finally:
    time.sleep(8)
    browser.quit()