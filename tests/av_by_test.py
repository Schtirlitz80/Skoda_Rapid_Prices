from unittest import TestCase, main

from av_by import get_pages_htmls, get_cars_info_list

class AvByTest(TestCase):
    def test_get_pages_htmls(self):
        """
        + 1) get_pages_html_list возвращает список
        + 2) все элементы списка - тексты
        + 3) все тексты являются html разметкой
        :return:
        """
        self.assertEqual(type(get_pages_htmls()), list)

        for element in get_pages_htmls():
            self.assertEqual(type(element), str)
            self.assertTrue('HTML' in element.upper())

    def test_get_cars_info_list(self):
        """
        1) возвращает список
        2) все элементы списка - словари
        :return:
        """
        self.assertEqual(type(get_cars_info_list()), list)
        for element in get_cars_info_list():
            self.assertEqual(type(element), dict)



if __name__ == '__main__':
    main()
