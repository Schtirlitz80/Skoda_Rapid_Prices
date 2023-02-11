from bs4 import BeautifulSoup
import requests
import os.path


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def get_source_pages(url: str) -> str:
    """
    Returns an html text of the source url
    :param url:
    :return:
    """
    page = requests.get(url, headers=headers).text
    # print(page)
    return page


def main():
    pagination = 1
    if not os.path.exists('htmls'):
        os.mkdir('htmls')
    while True:
        url = f'https://cars.av.by/filter?brands[0][brand]=1126&brands[0][model]=2424&brands[0][generation]=2264&year[min]=2014&transmission_type=2&engine_type[0]=1&page={pagination}'
        page = get_source_pages(url)

        with open(f"htmls/source{pagination}.html", "w", encoding='utf-8') as file:
            file.write(page)

        bs = BeautifulSoup(page, 'lxml')

        if bs.find('span', class_ = 'button__text', string = 'Показать ещё') == None: #больше нет страниц (эта - последняя)
            break

        pagination += 1


if __name__ == '__main__':
    main()
