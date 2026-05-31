import requests
from bs4 import BeautifulSoup
import json

url = "http://quotes.toscrape.com"
response = requests.get(url)
quotes_data = []

if response.status_code == 200:
    print('Сайт загружен, продолжаем...')

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f'Цитата: {text}')
        print(f'Автор: {author}')
        print('---')
        quotes_data.append({
            'text': text,
            'author': author,
        })
    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(quotes_data, f, ensure_ascii=False, indent=4)
        print(f'Цитаты сохранены')
else:
    print(f'Ошибка {response.status_code}')