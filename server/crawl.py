from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db="lunch_db")
cur = conn.cursor()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://map.kakao.com/?q=%EC%9D%B4%EB%8F%84%EA%B3%B0%ED%83%95%20%EB%B3%B8%EC%A0%90%20%EA%B7%BC%EC%B2%98%20%EC%8B%9D%EB%8B%B9")

time.sleep(3)

def get_menus (title):
    menus = {}
    try:
        more_button = driver.find_element(By.CSS_SELECTOR, '#mArticle > div.cont_menu > a')
        more_button.send_keys(Keys.ENTER)
    except:
        print('hi')

    names = driver.find_elements(By.XPATH, '//*[@id="mArticle"]/div/ul/li/div/span')
    prices = driver.find_elements(By.XPATH, '//*[@id="mArticle"]/div/ul/li/div/em')
    prices2 = driver.find_elements(By.CSS_SELECTOR, 'em.price_menu')

    menus['메뉴'] = []
    menus['가격'] = []

    for i in range(len(names)):
        menus['메뉴'].append(names[i].text)

        if prices[i].text != '':
            menus['가격'].append(prices[i].text)
            cur.execute('INSERT INTO menu (store, name, price) values ({},{},{})'.format('"' + title + '"', '"' + names[i].text + '"', '"' + prices[i].text + '"'))
        else:
            menus['가격'].append(prices2[i].text)
            cur.execute('insert into menu(store, name, price) values({},{},{})'.format('"' + title + '"', '"' + names[i].text + '"', '"' + prices2[i].text + '"'))
    conn.commit()
    return menus




def crawl (menus, title_arr, page, goal):
    if page == 1:
        more_place = driver.find_element(By.CSS_SELECTOR, "#info\.search\.place\.more")
        more_place.send_keys(Keys.ENTER)
        print('succeed', 'page = ', page)
        time.sleep(3)

    if page > 1:
        next_button = driver.find_element(By.CSS_SELECTOR, "#info\.search\.page\.next")
        next_button.send_keys(Keys.ENTER)
        print('succeed', 'page = ', page)
        time.sleep(3)

    if page > goal:
        print (menus, title_arr)
        return menus, title_arr


    titles = driver.find_elements(By.CSS_SELECTOR, "a.link_name")
    details = driver.find_elements(By.CSS_SELECTOR, "div.contact.clickArea > a.moreview")

    for i in range(len(titles)):
      print(titles[i].text)
      cur.execute('insert into store(name) values({})'.format('"' + titles[i].text + '"'))
      title = titles[i].text
      title_arr.append(title)
      print(title)
      details[i].send_keys(Keys.ENTER)
      time.sleep(3)
      driver.switch_to.window(driver.window_handles[-1])
      try:
        menus[title] = get_menus(title)
      except:
        print('이런')

#       menus[title] = get_menus(title)

      driver.close()
      driver.switch_to.window(driver.window_handles[0])
      print('hi')
    conn.commit()
    page += 1

    crawl(menus, title_arr, page, goal)




# more_place = driver.find_element(By.CSS_SELECTOR, "#info\.search\.place\.more")
#
# more_place.send_keys(Keys.ENTER)
# print('succeed')
#
# time.sleep(1)
#
# next_button = driver.find_element(By.CSS_SELECTOR, "#info\.search\.page\.next")
# next_button.send_keys(Keys.ENTER)
# print('succeed')
#
# time.sleep(1)
#
# next_button.send_keys(Keys.ENTER)
# print('succeed')



def main():



    menus = {}
    title_arr = []
    page = 0

    crawl(menus, title_arr, page, 15)

    conn.commit()
    driver.quit()


main()
conn.close()
