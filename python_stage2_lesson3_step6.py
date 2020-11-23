from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_class_name("trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    first_window = browser.window_handles[0]


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
