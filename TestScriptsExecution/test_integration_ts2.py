from src.URL.URLs import url_base, url_endpoint, url_booking_endpoint, url_auth_endpoint
from Test_scripts.API_wrapper import *
from src.helper.jsondata import payloadTestdata, Authentication, payloadPatchdata
from src.helper.headerdata import common_header
from src.helper.commonVerifications import *


class Test_APIBookings(object):

    def setup(self):
        print("Before Test")

    def test_auth_tc1(self):
        response = authToken_response(f"{url_base()}{url_auth_endpoint()}",
                                      headers=common_header(), payload=Authentication())
        print(f"{url_base()}{url_auth_endpoint()}")
        verify_http_code(response, 200)
        token_id = response.json()["token"]
        verify_AuthTokenid(tokenid=token_id)

    def test_get_bookings_tc2(self):
        response = get_response(f"{url_base()}", auth=None, headers=common_header(), in_json=False)
        verify_http_code(response, 200)

    def test_create_booking_tc3(self):
        response = post_response(f"{url_base()}{url_endpoint()}", auth=None, headers=common_header(),
                                 payload=payloadTestdata(), in_json=False)
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        print(booking_id)
        verify_key_forNotNullGreaterThanZero(booking_id)
        return booking_id

    # How to pass booking_id from above tc3.
    def test_patch_booking_tc4(self):
        response = post_response(f"{url_base()}{url_booking_endpoint().format(self.test_create_booking_tc3(1))}",
                                 auth=None,
                                 headers=common_header(), payload=payloadPatchdata(), in_json=False)
        print(f"{url_base()}{url_booking_endpoint().format(1)}")
        verify_http_code(response, 404)

    # How to pass booking_id from above tc1.
    def test_delete_booking_tc5(self):
        response = delete_response(f"{url_base()}{url_booking_endpoint().format(1)}", auth=None,
                                   headers=common_header(), in_json=False)
        print(f"{url_base()}{url_booking_endpoint().format(1)}")

    def tear_down(self):
        print("Complete")
