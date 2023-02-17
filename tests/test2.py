from av_by import get_car_cards_from_html
from database import put_list_into_db

with open('for_test.html', encoding='utf-8') as file:
    src_html = file.read()

cards_lst = get_car_cards_from_html(src_html)

# for card in cards_lst:
#     print(f'__________________\nCard:\n{card.text[:200]}')

# card = cards_lst[0]

new_cars = put_list_into_db(cards_lst)
print(new_cars)
