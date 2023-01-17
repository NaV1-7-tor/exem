import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

url = 'https://allo.ua/ua/roboty-pylesosy/'
headers = {'user-agent': fake_useragent.UserAgent().random}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
product = soup.find('div', class_='products-layout__container products-layout--grid')
products_all = product.find_all('div', class_='product-card')
for product in products_all:
    title = product.find('a', class_='product-card__title')
    price = product.find('div', class_='v-pb')
    print(price.text)
    print(title.text)
