import requests
from src.helper.json import payloadTestdata
from src.helper.header import common_header
from src.URL.URLs import url_base, url_endpoint, url_booking_endpoint


# Here, create the new booking data and confirm the booking id collected from the create api.
def post_CreateBooking_repos():
    response = requests.post(f"{url_base()}{url_endpoint()}", headers=common_header(), data=payloadTestdata())
    print(response.json())

    # Collect the booking id from json.
    booking_id = response.json()['bookingid']
    return booking_id


# Here, the booking id collected from the create api post_CreateBooking_repos().
def get_BookingIDs(booking_id):
    res = requests.get(f"{url_base()}{url_booking_endpoint().format(booking_id)}")
    print(res.json())
