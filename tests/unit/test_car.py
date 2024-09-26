from praktikum.car import Car


class TestCar:

    def test_car_weight_calculate(self, mock_engine, mock_frame):
        car = Car("TestCar")
        car.set_engine(mock_engine)
        car.set_frame(mock_frame)

        assert car.get_weight() == 1600
