import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import path
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# https://www.domain.com.au/real-estate-agents/?suburbs=mandurah-wa-6210%2Cbunbury-wa-6230%2Ceast-bunbury-wa-6230%2Csouth-bunbury-wa-6230%2Ceast-rockingham-wa-6168%2Cgeraldton-wa-6530%2Calbany-wa-6330%2Ckalgoorlie-wa-6430%2Csouth-kalgoorlie-wa-6430%2Cwest-kalgoorlie-wa-6430%2Cdarwin-city-nt-0800%2Cpalmerston-act-2913%2Cpalmerston-qld-4860%2Cpalmerston-city-nt-0830%2Ceast-palmerston-qld-4860%2Calice-springs-nt-0870%2Clitchfield-vic-3480%2Clitchfield-park-nt-0822%2Ctownsville-city-qld-4810%2Csouth-townsville-qld-4810%2Cthuringowa-central-qld-4817%2Ccairns-qld-4870%2Ccairns-north-qld-4870%2Ccairns-city-qld-4870%2Ctoowoomba-qld-4350%2Ctoowoomba-city-qld-4350%2Ceast-toowoomba-qld-4350%2Csouth-toowoomba-qld-4350%2Cnorth-toowoomba-qld-4350%2Ctoowoomba-west-qld-4350%2Crockhampton-qld-4701%2Crockhampton-city-qld-4700%2Cnorth-rockhampton-qld-4701%2Cwest-rockhampton-qld-4700%2Cmackay-qld-4740%2Cnorth-mackay-qld-4740%2Cwest-mackay-qld-4740%2Csouth-mackay-qld-4740%2Ceast-mackay-qld-4740%2Cmackay-harbour-qld-4740%2Cbundaberg-qld-4670%2Cbundaberg-north-qld-4670%2Cbundaberg-east-qld-4670%2Cbundaberg-south-qld-4670%2Cbundaberg-west-qld-4670%2Cbundaberg-central-qld-4670
driver = webdriver.Chrome('/Users/Prathmesh/Desktop/Chrome Driver/chromedriver.exe')
data = []
for i in range(1, 100):
    driver.get(f'https://www.domain.com.au/real-estate-agents/?page={i}&suburbs=mandurah-wa-6210%2Cbunbury-wa-6230%2Ceast-bunbury-wa-6230%2Csouth-bunbury-wa-6230%2Ceast-rockingham-wa-6168%2Cgeraldton-wa-6530%2Calbany-wa-6330%2Ckalgoorlie-wa-6430%2Csouth-kalgoorlie-wa-6430%2Cwest-kalgoorlie-wa-6430%2Cdarwin-city-nt-0800%2Cpalmerston-act-2913%2Cpalmerston-qld-4860%2Cpalmerston-city-nt-0830%2Ceast-palmerston-qld-4860%2Calice-springs-nt-0870%2Clitchfield-vic-3480%2Clitchfield-park-nt-0822%2Ctownsville-city-qld-4810%2Csouth-townsville-qld-4810%2Cthuringowa-central-qld-4817%2Ccairns-qld-4870%2Ccairns-north-qld-4870%2Ccairns-city-qld-4870%2Ctoowoomba-qld-4350%2Ctoowoomba-city-qld-4350%2Ceast-toowoomba-qld-4350%2Csouth-toowoomba-qld-4350%2Cnorth-toowoomba-qld-4350%2Ctoowoomba-west-qld-4350%2Crockhampton-qld-4701%2Crockhampton-city-qld-4700%2Cnorth-rockhampton-qld-4701%2Cwest-rockhampton-qld-4700%2Cmackay-qld-4740%2Cnorth-mackay-qld-4740%2Cwest-mackay-qld-4740%2Csouth-mackay-qld-4740%2Ceast-mackay-qld-4740%2Cmackay-harbour-qld-4740%2Cbundaberg-qld-4670%2Cbundaberg-north-qld-4670%2Cbundaberg-east-qld-4670%2Cbundaberg-south-qld-4670%2Cbundaberg-west-qld-4670%2Cbundaberg-central-qld-4670')
    links = driver.find_elements_by_class_name('css-j4qanj')

    for link in links:
        actual_link = link.find_element_by_tag_name('a').get_property('href')
        print(actual_link)
        data.append(actual_link)
print(len(data))
for item in data:
    driver.get(item)
    href = driver.find_element_by_class_name('css-1ulzglg').find_element_by_class_name('css-h339ia').find_element_by_class_name('css-b08a3j').find_element_by_tag_name('a').get_property('href')
    print(href)



