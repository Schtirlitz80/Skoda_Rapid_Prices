"""
Этот модуль предназначен для поиска машин Scoda Rapid I от 2014 года на сайте av.by.
Все функции объединяет функция get_car_info_list(), вызов которой возвращает список
словарей с машинами
"""

from bs4 import BeautifulSoup
import requests
from pprint import pprint


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def get_pages_html_list() -> list:
    pagination = 1
    lst = [] #список, который будет содержать тексты с html разметкой страниц с объявлениями на машины

    while True:
        url = f'https://cars.av.by/filter?brands[0][brand]=1126&brands[0][model]=2424&brands[0][generation]=2264&year[min]=2014&transmission_type=2&engine_type[0]=1&page={pagination}'
        page = requests.get(url, headers=headers).text
        lst.append(page)

        bs = BeautifulSoup(page, 'lxml')

        if bs.find('span', class_ = 'button__text', string = 'Показать ещё') == None: #больше нет страниц (эта - последняя)
            break

        pagination += 1

    return lst


def get_car_cards_from_html_page(html: str) -> list:
    """
    Gets all car cards from html page (one of all). Don't forget about pagination
    :param html:
    :return:
    """
    page_cards_list = []
    soup = BeautifulSoup(html, 'lxml')
    cards = soup.find_all('div', class_='listing-item')

    for card in cards:
        car_name = card.find('h3', class_='listing-item__title').text

        try:
            car_img = card.find('div', class_='listing-item__photo').find('img').get('data-src')
        except Exception as _ex:
            car_img = 'No image'

        year_descr_km_block = card.find('div', class_='listing-item__params').find_all('div')
        year = year_descr_km_block[0].text
        car_description = year_descr_km_block[1].text
        km = year_descr_km_block[2].text

        price = card.find('div', class_='listing-item__price').text
        price_usd = card.find('div', class_='listing-item__priceusd').text

        car_url = card.find('a').get('href')  # url будет уникальным идентификатором в базе данных
        car_url = f'https://cars.av.by{car_url}'

        location = card.find('div', class_='listing-item__location').text
        page_cards_list.append(
            {
                "car": car_name,
                "photo": car_img,
                "year": year,
                "descriprion": car_description,
                "km": km,
                "price": price,    # Нужно будет в дальнейшем проверять изменение цены и уведомлять об этом
                "usd_price": price_usd,
                "url": car_url,
                "location": location
            }
        )

    return page_cards_list


def get_car_info_list() -> list:
    """
    Получает список словарей с данными машин со всех страниц (пагинация)
    :return:
    """
    pages_lst = get_pages_html_list()

    cards_list = []

    for page_html in pages_lst:
        cards = get_car_cards_from_html_page(page_html)
        cards_list += cards

    return cards_list


def main():
    car_lst = get_car_info_list()

    print('Первый элемент списка машин (тестовая печать):')
    for item in car_lst[0]:
      print(f'{item}: {car_lst[0][item]}')


if __name__ == '__main__':
    main()
