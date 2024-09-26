from booking_api import BookingApi
from helper import BookingHelper


class TestUpdateBooking:

    def test_update_booking_total_price(self, create_booking, user_token):
        # Arrange
        test_body = BookingHelper.create_booking_body()
        test_body['totalprice'] = 10000

        # Act
        update_response = BookingApi.update_booking(create_booking.json()['bookingid'], test_body, user_token)

        # Assert
        assert update_response.status_code == 200 and update_response.json()['totalprice'] == 10000