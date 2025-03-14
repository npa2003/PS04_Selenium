from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get('https://en.wikipedia.org/wiki/Document_Object_Model')
browser.save_screenshot('dom.png')
time.sleep(5)

browser.get('https://ru.wikipedia.org/wiki/Selenium')
browser.save_screenshot('selenium.png')
time.sleep(5)
browser.refresh()
time.sleep(5)

browser.quit()