from main import get_car_cards_from_html


with open('for_test.html', encoding='utf-8') as file:
    src_html = file.read()

    cards_lst = get_car_cards_from_html(src_html)

    # for card in cards_lst:
    #     print(f'__________________\nCard:\n{card.text[:200]}')

    card = cards_lst[0]

    print(type(card))
    print(card)

    car_name = card.find('h3', class_='listing-item__title').text
    print(f'car_name: {car_name}')

    year_descr_km_block = card.find('div', class_='listing-item__params').find_all('div')
    year = year_descr_km_block[0].text
    print(f'year: {year}')
    car_description = year_descr_km_block[1].text
    print(f'car_descriprion: {car_description}')
    km = ''

