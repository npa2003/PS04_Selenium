from re import search

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time


browser = webdriver.Firefox()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

assert 'Википедия' in browser.title
time.sleep(1)

search_box = browser.find_element(By.ID, 'searchInput')
search_box.send_keys('Мороженое')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

a = browser.find_element(By.LINK_TEXT, 'Мороженое')
print(a)
print(a.text)
print(a.id)
print(a.accessible_name)
print(a.size)
print(a.aria_role)
print(a.tag_name)
print(a.location)
print(a.location_once_scrolled_into_view)
print(a.parent)
print(a.rect)
print(a.screenshot_as_base64)
print(a.screenshot_as_png)
with open('a_link.png','wb') as file:
    file.write(a.screenshot_as_png)
a.click()