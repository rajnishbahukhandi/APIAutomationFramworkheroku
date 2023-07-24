import requests
from src.URL.URLs import url_base, url_auth_endpoint
from src.helper.headerdata import common_header
from src.helper.jsondata import Authentication


# Here Update Booking information Based On Booking Id and pass the tokenid on it.
def put_AuthToken_repos():
    # pass the booking id into parameter from post_CreateBooking_repos at CreateBooking.py
    # Generate the token form Authentication API
    res = requests.post(f"{url_base()}{url_auth_endpoint()}", headers=common_header(), data=Authentication())
    # Store token into tokenid variable.
    tokenid = res.json()['token']
    print("Token id is:- ", tokenid)
    return tokenid


def verify_key(tokenid):
    assert len(tokenid) != 0, "tokenid is not Empty : " + put_AuthToken_repos()
    assert len(tokenid) > 0, "tokenid should be greater then zero : " + put_AuthToken_repos()