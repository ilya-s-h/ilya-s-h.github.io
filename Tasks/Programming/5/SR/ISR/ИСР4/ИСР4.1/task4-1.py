import re
import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

links = {
    'Московский район': 'https://www.bn.ru/kvartiry-vtorichka-moskovskij-rayon/',
    'Приморский район': 'https://www.bn.ru/kvartiry-vtorichka-primorskij-rayon/',
    'Пушкинский район': 'https://www.bn.ru/kvartiry-vtorichka-pushkinskij-rayon/'
}

def fetch_data():
    apartment_prices = []

    for district, link in links.items():
        for page in range(1, 26):
            page_link = link
            
            if page > 1:
                page_link += f'?page={page}'
                
            print(f'Fetching data from {page_link}...')
            
            res = requests.get(page_link)
            data = res.text

            soup = BeautifulSoup(data, 'html.parser')
            containers = soup.findAll('div', class_='catalog-item__container')
            
            for container in containers:
                catalog_price = container.find('div', class_='catalog-item__price')
                price = catalog_price.text.replace(' ', '').replace('₽', '')
                headline = container.find('div', class_='catalog-item__headline')
                square = re.findall('\d+\.\d+', headline.text)[0]
                    
                row = {
                    'district': district,
                    'square': float(square),
                    'price': int(price)
                }
                
                apartment_prices.append(row)
                
    apartment_prices = sorted(apartment_prices, key=lambda x: x['square'])
    return apartment_prices


def save_csv(apartment_prices, filename='apartment-prices.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['district', 'square', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(apartment_prices)


def load_csv(filename='apartment-prices.csv'):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['square'] = float(row['square'])
            row['price'] = int(row['price'])
            data.append(row)
    return data


def plotter(apartment_prices):
    districts = set(d['district'] for d in apartment_prices)
    for district in districts:
        squares = [d['square'] for d in apartment_prices if d['district'] == district]
        prices = [d['price'] for d in apartment_prices if d['district'] == district]
        plt.scatter(squares, prices)
        plt.ticklabel_format(style='plain')
        plt.title(f'Цены на недвижимость ({district})')
        plt.xlabel('Площадь квартиры')
        plt.ylabel('Цена')
        plt.show()


if __name__ == '__main__':
    apartment_prices = fetch_data()
    save_csv(apartment_prices)

    apartment_prices = load_csv()
    plotter(apartment_prices)
