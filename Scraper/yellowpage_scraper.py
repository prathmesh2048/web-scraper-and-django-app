import requests
import pandas as pd
from bs4 import BeautifulSoup

url_list = []
for j in range(1, 51):
    BASE_URL = f'https://www.yellowpages.com/search?search_terms=broker&geo_location_terms=Newark%2C%20NJ&page={j}'
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find_all('div', class_='result')
    for i in link:
        info = i.find('div', class_='info').find('h2', class_='n').find('a').get('href')
        url = 'http://www.yellowpages.com' + info
        url_list.append(url)
# print(len(url_list))
yellow_pages_list = []
title_list = []
address_list = []
phone_number_list = []
website_link_list = []
Email_list = []
reviews_list = []
rating_list = []
for items in url_list:
    BASE_URL = items
    page1 = requests.get(BASE_URL)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    upper_data = soup1.find('header', id='main-header')
    try:
        title = upper_data.find('div', class_='sales-info').text
    except:
        title = ''
    try:
        address = upper_data.find('div', class_='contact').h2.text
    except:
        address = ''
    try:
        phone_number = upper_data.find('div', class_='contact').find('p', class_='phone').text
    except:
        phone_number = ''
    try:
        years_in_business = upper_data.find('div', class_='years-in-business').text
    except:
        years_in_business = ''
    try:
        reviews = upper_data.find('section', class_='ratings').a.text
        if 'Be the first to review!' in reviews:
            reviews = 'No reviews available'
    except:
        reviews = ''
    try:
        rating1 = upper_data.find('section', class_='ratings').a.find('div')
        rating2 = f'{rating1}'
        rating = rating2.split()[2].split('"')[0]
    except:
        rating = ''
    try:
        lower_data = upper_data.find('div', class_='business-card-footer')
        try:
            website_link = lower_data.find('a', class_='primary-btn website-link').get('href')
        except:
            website_link = ''
        try:
            Email = lower_data.find('a', class_='email-business').get('href')
        except:
            Email = ''
    except:
        lower_data = ''

    print(items)
    print(years_in_business)
    print(title)
    print(address)
    print(phone_number)
    print(website_link)
    print(Email)
    print(rating)
    print(reviews)
    print('')
    print('')
    yellow_pages_list.append(items)
    title_list.append(title)
    address_list.append(address)
    phone_number_list.append(phone_number)
    website_link_list.append(website_link)
    Email_list.append(Email)
    reviews_list.append(reviews)
    rating_list.append(rating)
yellow_data = pd.DataFrame(
    {
        'title': title_list,
        'phone number': phone_number_list,
        'website': website_link_list ,
        'Email': Email_list ,
        'Address': address_list,
        'link to yellow pages': yellow_pages_list,
        'reviews': reviews_list,
        'rating': rating_list,

    }
)
yellow_data.to_csv('yellow1.csv')