from faker import Faker


class Helpers:
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = fake.password()
