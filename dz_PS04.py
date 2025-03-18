from re import search

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time

#search_text = input ('Введите текст для поиска:')
search_text = 'мороженое'

browser = webdriver.Firefox()
browser.get('https://ru.wikipedia.org/')
time.sleep(1)
assert 'Википедия' in browser.title

search_box = browser.find_element(By.ID, 'searchInput')
search_box.send_keys(search_text)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

lst = []
lst = browser.find_elements(By.CSS_SELECTOR, 'div.mw-search-result-heading') # ищем и создаём список с результатами поиска по DIV
h_name = [] # название
h_href = [] # ссылка
for txt in lst: # создаём словари с списками наименований и ссылок
    h_name.append(txt.text)
    h_href.append(txt.find_element(By.TAG_NAME, 'a').get_attribute('href'))   # по тегу 'a' внутри DIV

for n in range(len(h_name)):
    print(f'{n}. Название: {h_name[n]}')
    print(f'Ссылка: {h_href[n]}\n')

p1 = 1000000000
while p1 != 'q':
    if p1 == 'q':
        continue
    try:
        i = int(p1)
    except:
        print('Введите номер ссылки или "q" для вывода!')
        i = 1000000000

    if i < len(h_href):
        browser.get(h_href[i])
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs: # Для перебора пишем цикл
            print(paragraph.text)
            input()

    if i != 1000000000:
        for n in range(len(h_name)):
            print(f'{n}. Название: {h_name[n]}')
            print(f'Ссылка: {h_href[n]}\n')
    p1 = input('Введите номер ссылки для вывода ("q" для выхода): ')

print('Завершение программы. До свидания!')











# выводим на печать разные свойства найденной ссылки
# print(a)
# print(a.text)
# print(a.id)
# print(a.accessible_name)
# print(a.size)
# print(a.aria_role)
# print(a.tag_name)
# print(a.location)
# print(a.location_once_scrolled_into_view)
# print(a.parent)
# print(a.rect)
# print(a.screenshot_as_base64)
# print(a.screenshot_as_png)
# with open('a_link.png','wb') as file: # записываем в файл картинку самой ссылки
#     file.write(a.screenshot_as_png)
