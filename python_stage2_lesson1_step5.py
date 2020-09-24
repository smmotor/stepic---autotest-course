from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)

    input_answer =browser.find_element_by_css_selector("[id='answer']")
    input_answer.send_keys(y)

    option_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option_checkbox.click()
    option_radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    option_radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    
finally:
    time.sleep(10)
    browser.quit()
