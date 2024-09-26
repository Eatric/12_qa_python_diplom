from booking_api import BookingApi
from data import BookingData


class TestAuthUser:

    def test_auth_user(self):
        auth_response = BookingApi.auth_user(BookingData.AUTH_BODY)

        assert auth_response.status_code == 200 and auth_response.json()['token'] is not None