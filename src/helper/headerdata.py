# from Test_scripts.Authtoken import put_AuthToken_repos


def common_header():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    return headers




# def tokenHeader_json(tokenid):
#     # Pass the token into the headers.
#     headers_json = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#         'Cookie': 'token={0}'.format(tokenid)
#     }
#
#     return headers_json
#
#
# tokenHeader_json(put_AuthToken_repos)
