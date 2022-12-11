from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    option1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    option1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()