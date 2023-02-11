from bs4 import BeautifulSoup
import requests
import time


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


def get_elements_from_html(filename: str) -> list:
    with open(f'htmls/{filename}', encoding='utf-8') as file:
        src = file.read()

    print(src)


def main():
    # get_pages_url()

    pages_lst = get_pages_html_list()

    # for page in pages_lst:
    #     print(page[:2000])
    #     time.sleep(5)



if __name__ == '__main__':
    main()
