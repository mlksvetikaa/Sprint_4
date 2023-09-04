from faker import Faker
import random
import datetime


class Questions:
    QUESTIONS_LIST = [
        (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, "Пока что у нас так: один заказ — один самокат."
                " Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня."
                " Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."
                " Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, "Самокат приезжает к вам с полной зарядкой."
                " Этого хватает на восемь суток — даже если будете кататься без передышек и во сне."
                " Зарядка не понадобится."),
        (7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ]

class Registration:
    def fake_person_info():
        fake = Faker('ru_RU')
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.street_name()
        fake_person = {
            'firstname': first_name,
            'lastname': last_name,
            'address': address,
            'subway_station': 'Черкизовская',
        }
        return fake_person

class PhoneNumber:
    def get_phone_number():
        return random.randint(79000000000, 79999999999)

class Date:
    def get_date_today():
        return datetime.date.today().strftime('%d.%m.%Y')

    def get_date_tomorrow():
        return (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d.%m.%Y')

class RentalData:
    RENTAL_DATA_1 = {
        'rental_start_date': '01.09.2023',
        'rental_period': "one",
        'scooter_color': 'grey',
        'comment': 'Можете не торопиться!'
    }

    RENTAL_DATA_2 = {
        'rental_start_date': '01.09.2024',
        'rental_period': "two",
        'scooter_color': 'black',
        'comment': 'Можно, пожалуйста, быстрее!'
    }

class TextData:
    HEADER_TEXT = 'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'
    SUCCESSFUL_ORDER_TEXT = 'Заказ оформлен'