import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

titles = list()
prices = list()
prices_ozon_card = list()
prices_sale = list()
urls = list()
new = list()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url='https://www.ozon.ru/seller/smart-elektroniks-484216/products/?miniapp=seller_484216&sorting=new')
driver.implicitly_wait(15)
html = driver.page_source
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
soup = BeautifulSoup(html, "html.parser")
elements = soup.find_all("div",{"y4j yj5"})

for element in elements:
    titles.append(element.find_next("span",{"eh9 he9 ei ie1 tsBodyL j4v"}).text)
    prices_sale.append(element.find_next("span",{"_32-b1 _32-a5"}).text)
    prices.append(element.find_next("span",{"_32-a2"}).text)
    prices_ozon_card.append(element.find_next("span",{"_33-a0"}))
    # new.append(element.find_next('div',{'jy6'}).find_next('span',{'e0f'}).find_next('span'))

# print(new)

df = pd.DataFrame({"title":titles,
                   "price":prices,
                   "prices_sale":prices_sale,
                   "prices_ozon_card":prices_ozon_card

                   })

df.to_excel("result.xlsx")