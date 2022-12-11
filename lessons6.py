from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    y = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = browser.find_element(By.CSS_SELECTOR, "#num2")
    y_Num = int(y.text)
    x_Num = int(x.text)
    z = str(int(y_Num)+int(x_Num))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()