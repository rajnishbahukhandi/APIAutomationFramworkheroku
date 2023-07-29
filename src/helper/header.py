# from TestScriptsExecution.test_integration_ts2 import Test_APIBookings


def common_header():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    return headers


# def common_tokenHeader():
#     # Pass the token into the headers.
#     token_id1 = Test_APIBookings.static_var_Token
#     headers_json = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#         'Cookie': 'token={0}'.format(token_id1)
#     }
#     return headers_json
