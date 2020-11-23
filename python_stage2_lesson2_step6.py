from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    
    
    #ввод ответа в текстовое поле 
    input_answer = browser.find_element_by_css_selector("[id='answer']")
    input_answer.send_keys(y)


    #прокрутка страницы с помощью return arguments[0].scrollIntoView(true)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    #нажатие чекбокса(квадрат) и радиобаттона(круглый) 
    option_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option_checkbox.click()
    option_radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    option_radiobutton.click()
    
    
    button.click()

    
finally:
    time.sleep(10)
    browser.quit()
