from src.URL.URLs import url_base, url_endpoint, url_booking_endpoint, url_auth_endpoint
from Test_scripts.Wrappedscripts.API_wrapper import *
from src.helper.json import *
from src.helper.header import *
from src.helper.commonVerifications import *
from Test_scripts.Wrappedscripts.API_wrapper import post_response


# The testcase will be written by the user to use the Wrappedscripts file from Test_Scripts and the Helper file.

class Test_APIBookings:
    # Make the static variable for id and token. Static variable is shared among all instances of a class,
    # rather than being unique to each instance.
    # It belongs to the class itself rather than any particular instance of the class.
    static_var_id = 0
    static_var_Token = 0

    def setup(self):
        print("Before Test")

    def test_authorization_TC1(self):
        response = authToken_response(f"{url_base()}{url_auth_endpoint()}",
                                      headers=common_header(), payload=payloadAuthentication())
        verify_http_codeStatus(response, 200)
        token_id = response.json()["token"]
        # Assign the returned value of tokenid from the JSON response to the static token variable.
        Test_APIBookings.static_var_Token = token_id
        # Verify the verifications by calling the commonVerifiaction file.
        verify_AuthTokenid(tokenid=token_id)
        verify_responseTime(response)
        # Return the tokenId and save it in the static variable for the token.
        return token_id

    def test_create_booking_TC2(self):
        response = post_response(f"{url_base()}{url_endpoint()}", auth=None, headers=common_header(),
                                 payload=payloadTestdata_faker_post_put(), in_json=False)
        booking_id = response.json()["bookingid"]
        # Assign the returned value of bookingid from the JSON response to the static id variable.
        Test_APIBookings.static_var_id = booking_id
        # Verify the verifications by calling the commonVerifiaction file.
        verify_http_codeStatus(response, 200)
        verify_key_forNotNullGreaterThanZero(booking_id)
        verify_responseTime(response)
        print(response.json())
        # Return the tokenId and save it in the static variable for the token.
        return booking_id

    def test_put_bookings_TC3(self):
        # Use the format method to insert the static token into the headers.
        post_token_id = Test_APIBookings.static_var_Token
        json_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': 'token={0}'.format(post_token_id)
        }
        # Call the static variable of id from within the class and assign it to a variable.
        bookingidGetfromPost = Test_APIBookings.static_var_id
        response = put_response(f"{url_base()}{url_booking_endpoint().format(bookingidGetfromPost)}",
                                auth=None, headers=json_headers, payload=payloadTestdata_faker_post_put(),
                                in_json=False)
        # Verify the verifications by calling the commonVerifiaction file.
        verify_http_codeStatus(response, 200)
        verify_responseTime(response)
        print(response.json())

    def test_patch_booking_TC4(self):
        # Call the static variable of id from within the class and assign it to a variable.
        post_token_id = Test_APIBookings.static_var_Token
        json_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': 'token={0}'.format(post_token_id)
        }
        bookingidGetfromPost = Test_APIBookings.static_var_id
        response = patch_response(f"{url_base()}{url_booking_endpoint().format(bookingidGetfromPost)}",
                                  auth=None, headers=json_headers, payload=payloadTestdata_Patch(), in_json=False)
        # Verify the verifications by calling the commonVerifiaction file.
        verify_http_codeStatus(response, 200)
        verify_responseTime(response)
        print(response.json())

    def test_delete_booking_TC5(self):
        # Call the static variable of id from within the class and assign it to a variable.
        bookingidGetfromPost = Test_APIBookings.static_var_id
        response = delete_response(f"{url_base()}{url_booking_endpoint().format(bookingidGetfromPost)}", auth=None,
                                   headers=common_header(), in_json=False)
        # Verify the verifications by calling the commonVerifiaction file.
        verify_http_codesError(response, 403)
        verify_responseTime(response)

    def test_get_bookings_TC6(self):
        # Call the static variable of id from within the class and assign it to a variable.
        bookingidGetfromPost = Test_APIBookings.static_var_id
        response = get_response(f"{url_base()}{url_booking_endpoint().format(bookingidGetfromPost)}", auth=None,
                                headers=common_header(), in_json=False)
        # Verify the verifications by calling the commonVerifiaction file.
        verify_http_codeStatus(response, 200)
        verify_responseTime(response)
        print(response.json())

    def tear_down(self):
        print("Complete")
