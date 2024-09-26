from unittest.mock import Mock

import pytest
from selenium import webdriver

from booking_api import BookingApi
from data import BookingData
from helper import BookingHelper
from praktikum.colors import Color

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(BookingData.URL)

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def user_token():
    auth_response = BookingApi.auth_user(BookingData.AUTH_BODY)

    return auth_response.json()['token']

@pytest.fixture(scope='function')
def create_booking(user_token):
    created_booking = BookingApi.create_booking(BookingHelper.create_booking_body())

    yield created_booking

    BookingApi.delete_booking(created_booking.json()['bookingid'], user_token)


@pytest.fixture(scope='function')
def mock_engine():
    engine = Mock()
    engine.get_name.return_value = "MockEngine"
    engine.get_weight.return_value = 500

    return engine


@pytest.fixture(scope='function')
def mock_frame():
    frame = Mock()
    frame.get_color.return_value = Color.RED
    frame.get_weight.return_value = 300

    return frame