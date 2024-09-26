from faker import Faker

from data import BookingData


class BookingHelper:
    @staticmethod
    def create_booking_body():
        fake = Faker()

        booking_body = BookingData.CREATE_BOOKING_BODY.copy()

        booking_body['firstname'] = fake.name()
        booking_body['lastname'] = fake.name()

        return booking_body