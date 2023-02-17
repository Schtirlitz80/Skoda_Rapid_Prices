import os
from unittest import TestCase, main

from database import put_list_into_db


class DatabaseTest(TestCase):
    def test_put_list_into_db(self):
        """
        1. Создание базы, если не существует
        """
        if os.path.exists('cars_av_by.db'):
            os.remove('cars_av_by.db')

        lst = [{'car': 'Skoda Rapid I', 'photo': 'https://avcdn.av.by/advertpreview/0001/6236/0814.jpg', 'year': '2017\xa0г.', 'description': 'механика, 1.6\xa0л, бензин, лифтбек', 'km': '107\u2009000\xa0км', 'price': '28\u2009541\xa0р.', 'usd_price': '≈\xa010\u2009200\xa0$', 'url': 'https://cars.av.by/skoda/rapid/103282170', 'location': 'Могилев'}, {'car': 'Skoda Rapid I', 'photo': 'https://avcdn.av.by/advertpreview/0001/6762/5211.jpg', 'year': '2016\xa0г.', 'description': 'механика, 1.6\xa0л, бензин, лифтбек', 'km': '101\u2009000\xa0км', 'price': '36\u2009936\xa0р.', 'usd_price': '≈\xa013\u2009200\xa0$', 'url': 'https://cars.av.by/skoda/rapid/102690271', 'location': 'Брест'}, {'car': 'Skoda Rapid I', 'photo': 'https://avcdn.av.by/advertpreview/0001/7533/5178.jpg', 'year': '2014\xa0г.', 'description': 'механика, 1.6\xa0л, бензин, лифтбек', 'km': '95\u2009000\xa0км', 'price': '32\u2009179\xa0р.', 'usd_price': '≈\xa011\u2009500\xa0$', 'url': 'https://cars.av.by/skoda/rapid/103288291', 'location': 'Гомель'}, {'car': 'Skoda Rapid I', 'photo': 'https://avcdn.av.by/advertpreview/0001/7720/8812.jpg', 'year': '2014\xa0г.', 'description': 'механика, 1.6\xa0л, бензин, лифтбек', 'km': '170\u2009000\xa0км', 'price': '30\u2009640\xa0р.', 'usd_price': '≈\xa010\u2009950\xa0$', 'url': 'https://cars.av.by/skoda/rapid/103785096', 'location': 'Минск'}, {'car': 'Skoda Rapid I', 'photo': 'https://avcdn.av.by/advertpreview/0001/7725/6371.jpg', 'year': '2015\xa0г.', 'description': 'механика, 1.6\xa0л, бензин, лифтбек', 'km': '136\u2009000\xa0км', 'price': '32\u2009039\xa0р.', 'usd_price': '≈\xa011\u2009450\xa0$', 'url': 'https://cars.av.by/skoda/rapid/103635138', 'location': 'Минск'}]

        put_list_into_db(lst)

        self.assertTrue(os.path.exists('cars_av_by.db'))


if __name__ == '__main__':
    main()
