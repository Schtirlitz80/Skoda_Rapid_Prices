from main import get_car_cards_from_html_page
from pprint import pprint


with open('for_test.html', encoding='utf-8') as file:
    src_html = file.read()

cards_lst = get_car_cards_from_html_page(src_html)

# for card in cards_lst:
#     print(f'__________________\nCard:\n{card.text[:200]}')

card = cards_lst[0]

for item in card:
    print(f"{item}: {card[item]}")

