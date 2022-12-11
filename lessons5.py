from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = input1.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    option1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    option1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(11)
    browser.quit()