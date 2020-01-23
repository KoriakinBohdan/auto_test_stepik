from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    link = "https://dassuranceproducts.aaps.deloitte.com/registration/sbp"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(15)


    select = browser.find_element_by_css_selector(".css-1hwfws3").click()
    time.sleep(2)
    select2 = browser.find_element_by_id("react-select-3-option-1").click()
    next = browser.find_element_by_css_selector('button.btn-primary').click()
    Check_box = browser.find_element_by_css_selector("label.Checkbox_label__2Z3is").click()
    time.sleep(1)
    next2 = browser.find_element_by_css_selector('button.btn-primary').click()
    Black_Scholes = browser.find_element_by_css_selector("[for='Black-Scholes TEST']").click()
    Monte_Carlo = browser.find_element_by_css_selector("[for='Monte Carlo TEST']").click()
    Binomial = browser.find_element_by_css_selector("[for='Binomial']").click()
    TSR = browser.find_element_by_css_selector("[for='TEST TSR Monitoring']").click()
    time.sleep(1)
    next3 = browser.find_element_by_css_selector('button.btn-primary').click()
    Email = browser.find_element_by_id("form-input-email-email").send_keys("testPython@gmail.com")
    First_name = browser.find_element_by_id("form-input-text-first-name").send_keys("Test")
    Last_name = browser.find_element_by_id("form-input-text-last-name").send_keys("Test1")
    Company = browser.find_element_by_id("form-input-text-company-full-legal-name").send_keys("TestCompany")
    Address = browser.find_element_by_id("form-input-text-address").send_keys("Grihorenka 23a")
    Country = browser.find_element_by_css_selector(".css-1hwfws3").click()
    Select_Country = browser.find_element_by_id("react-select-4-option-4").click()
    Town = browser.find_element_by_id("form-input-text-town-city").send_keys("kyiv")
    Zip = browser.find_element_by_id("form-input-text-zip-postal-code").send_keys("18000")
    Referral_Name = browser.find_element_by_id("form-input-text-referral-name").send_keys("N/A")
    Referral_Email = browser.find_element_by_id("form-input-email-referral-email").send_keys("N/A")
    time.sleep(2)
    next4 = browser.find_element_by_css_selector('button.btn-primary').click()
#    Confirmation_page = WebDriverWait(browser, 15).until(
#        EC.presence_of_element_located((By.TAG_NAME, "html")))
    Confirmation_text = browser.find_element_by_tag_name("h2")
    Confirmation_text = Confirmation_text.text
    assert "Thank you for submitting your application" == Confirmation_text


finally:

    time.sleep(20)
    browser.quit()