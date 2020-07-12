import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import path
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# driver = webdriver.Chrome('/Users/Prathmesh/Desktop/Chrome Driver/chromedriver.exe')
# Program to find the link to the particular book -:
'''list_of_pages = ['https://techknowledgebooks.com/product-category/sppu/']
for j in range(2, 11):
    text = f'https://techknowledgebooks.com/product-category/sppu/page/{j}/'
    list_of_pages.append(text)
for element in list_of_pages:
    page = requests.get(element)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find('div', class_="products row row-small large-columns-3 medium-columns-3 small-columns-2")
    link = links.find_all('div', class_='image-fade_in_back')
    for i in link:
        link1 = i.a.get('href')
        print(link1)
'''
page = requests.get('https://techknowledgebooks.com/product/advanced-c-programming-2/')
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('div', class_='col medium-6 small-12 large-6')[-1]
data1 = data.find_all('p')
for i in data1:
    final_data = i.text
    print(final_data)
    if 'Language :' in final_data:
        break
try:
    desc = soup.find('div', class_='woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content active')
    print(desc.text)
except:
    print("NOne")


