import requests
from src.helper.headerdata import common_header
from src.helper.jsondata import Authentication, update_testdata
from src.URL.URLs import url_base, url_auth_endpoint, url_booking_endpoint


# Here Update Booking information Based On Booking Id and pass the tokenid on it.
def put_UpdateBookingBasedOnBookingId_repos(booking_id):
    # pass the booking id into parameter from post_CreateBooking_repos at CreateBooking.py
    # Generate the token form Authentication API
    res = requests.post(f"{url_base()}{url_auth_endpoint()}", headers=common_header(), data=Authentication())
    # Store token into tokenid variable.
    tokenid = res.json()['token']

    # Pass the token into the headers.
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'token={0}'.format(tokenid)
       }
    # Update the booking data on newly created booking id.
    res = requests.put(f"{url_base()}{url_booking_endpoint().format(booking_id)}",
                       headers=headers, data=update_testdata())
    print(res.json())