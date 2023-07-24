# Set the base URL for the API
def url_base():
    url = "https://restful-booker.herokuapp.com"
    return url


# Set the endpoint for creating a booking
def url_endpoint():
    url = "/booking"
    return url


# Set the endpoint for getting a booking by ID
def url_booking_endpoint():
    url = "/booking/{}"
    return url


# Set the authentication endpoint
def url_auth_endpoint():
    url = "/auth"
    return url




# Set the base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com/booking/2365"

# Set the endpoint for creating a booking
BOOKING_ENDPOINT = "/booking"

# Set the endpoint for getting a booking by ID
GET_BOOKING_ENDPOINT = "/booking/{}"

# Set the authentication endpoint
AUTH_ENDPOINT = "/auth"
