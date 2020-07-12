import requests
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = ['http://www.pune.ws/in/?list=companies', 'http://www.pune.ws/in/?list=companies&s=2']
for i in BASE_URL:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all('div', class_='ebl')
    title = []
    desc = []
    address = []
    phone_number = []
    email = []
    for data in items:
        data0 = data.a.h2.text
        data1 = data.find_all('div')[0].text
        data2 = data.find_all('div')[1].text
        data3 = data.find_all('div')[2].text.split('|')[2]
        data4 = data.find_all('div')[2].a.attrs['href']
        title.append(data0)
        desc.append(data1)
        address.append(data2)
        phone_number.append(data3)
        email.append(data4)

    company = pd.DataFrame(
        {
            'title': title,
            'phone_number': phone_number,
            'email': email,
            'desc': desc,
            'address': address,
        }
    )
    print(company)
    company.to_excel("'fcompant {}'.xlsx")

# print(data.text)
'''import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import path
from selenium import webdriver

driver = webdriver.Chrome('/Users/Prathmesh/Desktop/Chrome Driver/chromedriver.exe')
driver.get('https://www.superimmo.com/location/corse/pieces-1-5?bedrooms_max=4&bedrooms_min=1&price_max=1000.0&price_min=100.0')
driver.quit()
BASE_URL = driver.execute_script("return document.documentElement.outerHTML")
# BASE_URL = 'https://www.superimmo.com/location/corse/pieces-1-5?bedrooms_max=4&bedrooms_min=1&price_max=1000.0&price_min=100.0'

# page = requests.get(BASE_URL)
soup = BeautifulSoup(BASE_URL, 'html.parser')'''