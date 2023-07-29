# from faker import Faker
# fake = Faker()


def payloadAuthentication():
    payload = {
            "username": "admin",
            "password": "password123"
            }
    return payload


def payloadTestdata():
    payload = {
        "firstname": "John",
        "lastname": "Dev",
        "totalprice": "500",
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-03-05",
            "checkout": "2023-03-12",
        },
        "additionalneeds": "Lunch"
    }
    return payload


def payloadTestdata_update():
    payload = {
        "firstname": "Rajnish",
        "lastname": "Bahukhandi",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-07-10",
            "checkout": "2023-07-15"
        },
        "additionalneeds": "Breakfast and lunch"
    }
    return payload


def payloadTestdata_Patch():
    payload = {
                  "firstname": "Omkar",
                  "lastname": "Ram",
              },
    return payload

# def payloadTestdata():
#     payload = {
#         "firstname": "Rahul",
#         "lastname": "Sharma",
#         "totalprice": "500",
#         "depositpaid": "88",
#         "bookingdates": {
#             "checkin": "2022-11-05",
#             "checkout": "2022-10-12",
#         },
#         "additionalneeds": "Lunch"
#     }
#     return payload


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
