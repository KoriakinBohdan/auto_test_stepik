from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # скрипт на скрол
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()
    input3 = browser.find_element_by_id('robotsRule')
    input3.click()
    input4 = browser.find_element_by_css_selector('button.btn')
    input4.click()

finally:

    time.sleep(10)
    browser.quit()