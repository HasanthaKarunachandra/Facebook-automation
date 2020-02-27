from selenium import webdriver

browser = webdriver.Chrome("D:\Project\python\selunima\Drivers\chromedriver.exe")

browser.get("http://www.facebook.com")

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")

username.send_keys("Your email")
password.send_keys("Your password")
submit.click()
