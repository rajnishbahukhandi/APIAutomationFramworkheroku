# Set the Base URL for the API.

# Set the Authentication endpoint.
def url_auth_endpoint():
    url = "/auth"
    return url


# Set the Base Url.
def url_base():
    url = "https://restful-booker.herokuapp.com"
    return url


# Set the endpoint for creating a booking.
def url_endpoint():
    url = "/booking"
    return url


# Set the endpoint for getting a booking by ID.
def url_booking_endpoint():
    url = "/booking/{}"
    return url
