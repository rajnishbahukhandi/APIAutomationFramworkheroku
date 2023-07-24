# HTTP Status Code

def verify_http_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expected HTTP Status : " + expected_data


def verify_key_forNotNullGreaterThanZero(key):
    assert key != 0, "tokenid is not Empty : " + key
    assert key > 0, "tokenid should be greater then zero : " + key


def verify_AuthTokenid(tokenid):
    assert len(tokenid) != 0, "tokenid is not Empty : " + tokenid
    assert len(tokenid) > 0, "tokenid should be greater then zero : " + tokenid
