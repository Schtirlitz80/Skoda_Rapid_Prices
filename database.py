import sqlite3


def put_list_into_db(lst: list) -> list:
    """
    Получает список машин, пытается добавить их в базу данных.
    Если уникальный url объявления уже есть в базе, то запись не добавляется.
    Возвращает список машин, которых не было в базе и которые были добавлены
    :param lst:
    :return:
    """
    d_base = sqlite3.connect('cars_av_by.db')
    with d_base:
        cur = d_base.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS av_cars(
                                        id INTEGER PRIMARY KEY,
                                        car_name TEXT,
                                        car_img TEXT,
                                        car_year TEXT,
                                        car_description TEXT,
                                        km TEXT,
                                        price TEXT,
                                        price_usd TEXT,
                                        car_url TEXT unique,
                                        location TEXT
                        )"""
        )

        new_cars_lst = []

        for car in lst:
            car_name = car["car"]
            car_img = car["photo"]
            car_year = car["year"]
            car_description = car["description"]
            km = car["km"]
            price = car["price"]
            price_usd = car["usd_price"]
            car_url = car["url"]
            location = car["location"]

            sql_query = f"""INSERT INTO av_cars(car_name, car_img, car_year, car_description, km, price, price_usd, car_url, location)
                                VALUES ('{car_name}', '{car_img}', '{car_year}', '{car_description}', '{km}', '{price}', '{price_usd}', '{car_url}', '{location}')
                        """
            try:
                cur.execute(sql_query)
                new_cars_lst.append(car)
            except Exception as _ex:
                print(_ex)

        d_base.commit()

    return new_cars_lst
