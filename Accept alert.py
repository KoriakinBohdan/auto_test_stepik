from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("button.btn")
    input1.click()
    alert = browser.switch_to_alert()
    alert.accept()
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
