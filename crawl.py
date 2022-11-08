from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


def get_menus ():
    menus = {}
    names = driver.find_elements(By.CSS_SELECTOR, "#mArticle > div.cont_menu > ul > li > div > span")
    prices = driver.find_elements(By.CSS_SELECTOR, "#mArticle > div.cont_menu > ul > li > div > em.price_menu")

    for i in range(len(names)):
        menus[names[i].text] = prices[i].text

    return menus



chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://map.kakao.com/?q=%EC%9D%B4%EB%8F%84%EA%B3%B0%ED%83%95%20%EB%B3%B8%EC%A0%90%20%EA%B7%BC%EC%B2%98%20%EC%8B%9D%EB%8B%B9")

time.sleep(3)


menus = {}
page = 0

def main_def (menus, page):
    if page == 1:
        more_place = driver.find_element(By.CSS_SELECTOR, "#info\.search\.place\.more")
        more_place.send_keys(Keys.ENTER)
        print('succeed', 'page = ', page)
        time.sleep(2)

    if page > 1:
        next_button = driver.find_element(By.CSS_SELECTOR, "#info\.search\.page\.next")
        next_button.send_keys(Keys.ENTER)
        print('succeed', 'page = ', page)
        time.sleep(2)

    if page > 10:
        return menus


    titles = driver.find_elements(By.CSS_SELECTOR, "a.link_name")
    details = driver.find_elements(By.CSS_SELECTOR, "div.contact.clickArea > a.moreview")

    for i in range(len(titles)):
      print(titles[i].text)
      title = titles[i].text
      details[i].send_keys(Keys.ENTER)
      time.sleep(2)
      driver.switch_to.window(driver.window_handles[-1])
      menus[title] = get_menus()
      print(menus)
      driver.close()
      driver.switch_to.window(driver.window_handles[0])
      print('hi')

    page += 1

    main_def(menus, page)

result = main_def(menus, page)
print(result)

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







driver.quit()
