import json
from faker import Faker

fake = Faker()


def generate_testdata():
    payload = json.dumps({
        "firstname": "Rahul",
        "lastname": "Sharma",
        "totalprice": "500",
        "depositpaid": "88",
        "bookingdates": {
            "checkin": "2022-11-05",
            "checkout": "2022-10-12",
        },
        "additionalneeds": "Lunch"
    })
    return payload


def update_testdata():
    payload = json.dumps({
        "firstname": "Rajnish Shiv",
        "lastname": "Bahukhandi Vishnu",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-05",
            "checkout": "2023-04-01"
        },
        "additionalneeds": "Breakfast"
    })
    return payload


def Authentication():
    payload = json.dumps({
        "username": "admin",
        "password": "password123"
    })
    return payload


def payloadTestdata():
    payload = {
        "firstname": "Rahul",
        "lastname": "Sharma",
        "totalprice": "500",
        "depositpaid": "88",
        "bookingdates": {
            "checkin": "2022-11-05",
            "checkout": "2022-10-12",
        },
        "additionalneeds": "Lunch"
    }
    return payload


def payloadPatchdata():
    payload = {
        "firstname": "Shiva",
        "lastname": "Sambhu",
        },
    return payload

    # Using faker
    # payload = json.dumps({
    #     "firstname": fake.first_name(),
    #     "lastname": fake.last_name(),
    #     "totalprice": fake.pyint(min_value=10, max_value=1000),
    #     "depositpaid": fake.pybool,
    #     "bookingdates": {
    #         "checkin": str(fake.date_between(start_date='-30d', end_date='today')),
    #         "checkout": str(fake.date_between(start_date='today', end_date='+30d')),
    #     },
    #     "additionalneeds": fake.word()
    # })
    # return payload
