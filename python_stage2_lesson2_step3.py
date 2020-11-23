from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    x_str = num1.text
    y_str = num2.text
    x_int = int(x_str)
    y_int = int(y_str)
    sum_int = x_int + y_int
    sum_str = str(sum_int)
    select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_visible_text('%s' % sum_str) #чем то Си напоминает
    select.select_by_value(sum_str)

   
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    
finally:
    time.sleep(10)
    browser.quit()
