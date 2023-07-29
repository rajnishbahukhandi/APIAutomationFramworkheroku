# Assertions: Python assert allow to sanity check the code.
# Common Verification file: Here verify the status code, empty value, null value, lenght of value.

def verify_http_codeStatus(response_data, expected_data):
    # assert response_data.status_code == expected_data, "Expected HTTP Status : " + expected_data
    assert response_data.status_code in [200, 201, 200], f'Expected status, but got {response_data.status_code}'


def verify_http_codesError(response_data, expected_data):
    # assert response_data.status_code == expected_data, "Expected HTTP Status : " + expected_data
    assert response_data.status_code in [403, 400, 500], f'Expected status, but got {response_data.status_code}'


def verify_key_forNotNullGreaterThanZero(key):
    assert key != 0, "tokenid is not Empty : " + key
    assert key > 0, "tokenid should be greater then zero : " + key


def verify_AuthTokenid(tokenid):
    assert len(tokenid) != 0, "tokenid is not Empty : " + tokenid
    assert len(tokenid) > 0, "tokenid should be greater then zero : " + tokenid


def verify_responseTime(response_data):
    assert response_data.elapsed.total_seconds() < 3
