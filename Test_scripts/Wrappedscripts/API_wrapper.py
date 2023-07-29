import json
import requests


# Abstraction and encapsulation.

def authToken_response(url, headers, payload):
    # pass the booking id into parameter from post_CreateBooking_repos at CreateBooking.py
    # Generate the token form Authentication API
    auth_response = requests.post(url=url, headers=headers, data=json.dumps(payload))
    return auth_response


def get_response(url, auth, headers, in_json):
    get_response = requests.get(url=url, auth=auth, headers=headers)
    if in_json is True:
        # in_json, means want response as a json then return response in json.
        return get_response.json()
    return get_response


def post_response(url, auth, headers, payload, in_json):
    post_response_data = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        # in_json, means want response as a json then return response in json.
        return post_response_data.json()
    return post_response_data


def put_response(url, auth, headers, payload, in_json):
    put_response_data = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data


def patch_response(url, auth, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        # in_json, means want response as a json then return response in json.
        return patch_response_data.json()
    return patch_response_data


def delete_response(url, auth, headers, in_json):
    delete_response_data = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        # in_json, means want response as a json then return response in json.
        return delete_response_data.json()
    return delete_response_data
