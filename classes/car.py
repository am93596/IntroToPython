class Car:
    _maximum_speed = 100
    _current_speed = 0

    def check_current_speed(self):
        return self._current_speed

    def accelerate(self, increase_by):
        if (self._current_speed+increase_by) <= self._maximum_speed:
            self._current_speed += increase_by
        else:
            print("\nMax speed reached. Cannot increase speed further.\n")

    def decelerate(self, decrease_by):
        if (self._current_speed-decrease_by) >= 0:
            self._current_speed -= decrease_by
        else:
            print("\nCar is stationary. Cannot slow down further.\n")


car1 = Car()
print(car1.check_current_speed())
car1.accelerate(102)
print(car1.check_current_speed())
car1.decelerate(100)
print(car1.check_current_speed())
car1.decelerate(2)
print(car1.check_current_speed())
