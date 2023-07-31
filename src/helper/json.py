from faker import Faker
fake = Faker()


def payloadAuthentication():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def payloadTestdata_faker_post_put():
    payload = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.pyint(min_value=10, max_value=1000),
        "depositpaid": fake.pybool(),
        "bookingdates": {
            "checkin": str(fake.date_between(start_date='-30d', end_date='today')),
            "checkout": str(fake.date_between(start_date='today', end_date='+30d')),
        },
        "additionalneeds": fake.word()
    }
    return payload


def payloadTestdata_Patch():
    payload = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
    }
    return payload
