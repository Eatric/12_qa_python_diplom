import requests

from data import BookingData
from endpoints import BookingEndpoints


class BookingApi:

    @staticmethod
    def auth_user(body):
        auth_response = requests.post(BookingData.URL + BookingEndpoints.AUTH_ENDPOINT, json=body)

        return auth_response

    @staticmethod
    def create_booking(body):
        create_response = requests.post(BookingData.URL + BookingEndpoints.CREATE_ENDPOINT, json=body)

        return create_response

    @staticmethod
    def update_booking(booking_id, body, token):
        update_response = requests.put(BookingData.URL + BookingEndpoints.UPDATE_ENDPOINT + str(booking_id), json=body, headers={
            'Cookie': 'token=' + token
        })

        return update_response

    @staticmethod
    def delete_booking(booking_id, token):
        delete_response = requests.delete(BookingData.URL + BookingEndpoints.DELETE_ENDPOINT + str(booking_id), headers={
            'Cookie': 'token=' + token
        })

        return delete_response