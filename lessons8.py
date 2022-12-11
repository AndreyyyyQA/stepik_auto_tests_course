from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Dick")
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input1.send_keys("Dick")
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input1.send_keys("Dick")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'dick.txt')
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(8)
    browser.quit()