from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input_name = browser.find_element_by_css_selector("[name='firstname']")
    input_name.send_keys("Test")
    input_lastname = browser.find_element_by_css_selector("[name='lastname']")
    input_lastname.send_keys("Testovich")
    input_email = browser.find_element_by_css_selector("[name='email']")
    input_email.send_keys("blabla@mail.ru")

    input_dirfile = browser.find_element_by_name("file")
    element = input_dirfile
                                                          
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
                                                          
    element.send_keys(file_path)                                                      
                                                              
    button = browser.find_element_by_css_selector("button.btn")
    button.click()                                                          



finally:
    time.sleep(10)
    browser.quit()

