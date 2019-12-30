from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc():
    return str(int(a) + int(b))


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_id("num1")
    a = a_element.text
    b_element = browser.find_element_by_id("num2")
    b = b_element.text
    y = calc()
    x = y
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(x)
    submit = browser.find_element_by_css_selector('button.btn')
    submit.click()
    
finally:

    time.sleep(10)
    browser.quit()
