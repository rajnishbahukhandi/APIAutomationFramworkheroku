import requests
from src.helper.jsondata import generate_testdata
from src.helper.headerdata import common_header
from src.URL.URLs import url_base, url_endpoint, url_booking_endpoint


# Here, create the new booking data and confirm the booking id collected from the create api.
def post_CreateBooking_repos():
    response = requests.post(f"{url_base()}{url_endpoint()}", headers=common_header(), data=generate_testdata())
    print(response.json())

    # Collect the booking id from json.
    booking_id = response.json()['bookingid']
    return booking_id


# Here, the booking id collected from the create api post_CreateBooking_repos().
def get_BookingIDs(booking_id):
    res = requests.get(f"{url_base()}{url_booking_endpoint().format(booking_id)}")
    print(res.json())