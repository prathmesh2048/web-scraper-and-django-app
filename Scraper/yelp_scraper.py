import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium import webdriver


url_list = []

for j in range(0, 12):
    BASE_URL = f'https://www.yelp.com/search?find_desc=Cbd%20Stores&find_loc=San%20Francisco%2C%20CA&ns=1&start={j}0'
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        divs = soup.find_all('div', class_='lemon--div__373c0__1mboc container__373c0__3HMKB hoverable__373c0__VqkG7 margin-t3__373c0__1l90z margin-b3__373c0__q1DuY padding-t3__373c0__1gw9E padding-r3__373c0__57InZ padding-b3__373c0__342DA padding-l3__373c0__1scQ0 border--top__373c0__3gXLy border--right__373c0__1n3Iv border--bottom__373c0__3qNtD border--left__373c0__d1B7K border-color--default__373c0__3-ifU')
        for i in divs:
            link = i.find('a', class_='lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE').get('href')
            final_url = f'https://www.yelp.com/{link}'
            url_list.append(final_url)

    except:
        divs = ''
popped_element = url_list.pop(0)
yelp_pages_list = []
title_list = []
zip_code_list = []
address_list = []
phone_number_list = []
website_link_list = []
reviews_list = []
rating_list = []
for items in url_list:
    BASE_URL1 = items
    page = requests.get(BASE_URL1)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        title = soup.find('h1', class_='lemon--h1__373c0__2ZHSL heading--h1__373c0__dvYgw undefined heading--inline__373c0__10ozy').text
    except:
        title = 'not available'
    try:
        rating = soup.find('div', class_='lemon--div__373c0__1mboc i-stars__373c0__1BRrc i-stars--large-4-half__373c0__3qH22 border-color--default__373c0__3-ifU overflow--hidden__373c0__2y4YK').get('aria-label')
    except:
        rating = 'not available'
    try:
        reviews = soup.find('p', class_='lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa- text-size--large__373c0__3t60B').text
    except:
        reviews = 'not available'
    try:
        website1 = soup.find('div', class_='lemon--div__373c0__1mboc island-section__373c0__3SUh7 border--top__373c0__3gXLy border-color--default__373c0__3-ifU')
        website2 = website1.find('a', class_='lemon--a__373c0__IEZFH link__373c0__1G70M link-color--blue-dark__373c0__85-Nu link-size--inherit__373c0__1VFlE').get('href')
        website = f'https://www.yelp.com/{website2}'
    except:
        website = 'not available'
    try:
        phone1 = soup.find('div', class_='lemon--div__373c0__1mboc padding-t3__373c0__1gw9E padding-r3__373c0__57InZ padding-b3__373c0__342DA padding-l3__373c0__1scQ0 border--top__373c0__3gXLy border--right__373c0__1n3Iv border--bottom__373c0__3qNtD border--left__373c0__d1B7K border-radius--regular__373c0__3KbYS background-color--white__373c0__2uyKj')
        phone2 = phone1.find_all('div', class_='lemon--div__373c0__1mboc island-section__373c0__3SUh7 border--top__373c0__3gXLy border-color--default__373c0__3-ifU')[1]
        phone3 = phone2.find('p', class_='lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa-').text
        phone = phone3
    except:
        phone = 'not available'
    try:
        address1 = soup.find('div', class_='lemon--div__373c0__1mboc padding-t2__373c0__11Iek padding-r2__373c0__28zpp padding-b2__373c0__34gV1 padding-l2__373c0__1Dr82 border-color--default__373c0__3-ifU')
        address = address1.find('div', class_='lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT arrange-unit-fill__373c0__3Sfw1 border-color--default__373c0__3-ifU').text
    except:
        address = 'not available'
    try:
        zip1 = soup.find('div', class_='lemon--div__373c0__1mboc padding-t2__373c0__11Iek padding-r2__373c0__28zpp padding-b2__373c0__34gV1 padding-l2__373c0__1Dr82 border-color--default__373c0__3-ifU')
        zip2 = zip1.find('div', class_='lemon--div__373c0__1mboc arrange-unit__373c0__o3tjT arrange-unit-fill__373c0__3Sfw1 border-color--default__373c0__3-ifU')
        zip3 = zip2.find_all('p', class_='lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz')[1].text
        zip4 = f'{zip3}'
        temp = re.findall(r'\d+', zip4)
        res = str(list(map(int, temp)))
        s = ''
        s = s.join(res)
        zip_code = f'{s}'
    except:
        zip_code = 'not available'
    print(items)
    print(title)
    print(rating)
    print(reviews)
    print(website)
    print(phone)
    print(address)
    print(zip_code)
    yelp_pages_list.append(items)
    title_list.append(title)
    rating_list.append(rating)
    reviews_list.append(reviews)
    website_link_list.append(website)
    phone_number_list.append(phone)
    address_list.append(address)
    zip_code_list.append(zip_code)

yelp_data = pd.DataFrame(
    {
        'title': title_list,
        'phone number': phone_number_list,
        'website': website_link_list ,
        'zip code': zip_code_list ,
        'Address': address_list,
        'link to yelp pages': yelp_pages_list,
        'reviews': reviews_list,
        'rating': rating_list,

    }
)
yelp_data.to_csv('yelp.csv')