from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("button.trollface")
    input1.click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()
finally:
    time.sleep(7)
    browser.quit()
