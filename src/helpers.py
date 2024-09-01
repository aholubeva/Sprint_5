import faker
import random


def get_sign_up_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password()
    incorrect_password = random.randint(0, 10000)
    return name, email, password, incorrect_password

