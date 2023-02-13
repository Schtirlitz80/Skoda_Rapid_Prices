import sqlite3


with open('cars_av_by.db', 'w', encoding='UTF-8') as file:
    db = sqlite3.connect(file)

    cursor = db.cursor()

    cursor.execute(
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


'''
car_name = car["car"]

car_img = car["photo"]
print(car_img)

year = car["year"]
car_description = car["descriprion"]
km = car["km"]
price = car["price"]
price_usd = car["usd_price"]
car_url = car["url"]
location = car["location"]

photo_caption = f'{car_name}\n{year}\n{car_description}\n{km}\n{price} ({price_usd})\n{car_url}\n{location}'
'''