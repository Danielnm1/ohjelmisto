import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        """Change current_speed by speed_change while keeping it between 0 and maximum_speed."""
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        """Increase travelled_distance based on current_speed for given hours."""
        self.travelled_distance += self.current_speed * hours


def race(cars):

    finished = False
    while not finished:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                finished = True
                break
    return cars


cars = [Car("ABC-123", 150), Car("XYZ-789", 180), Car("DEF-456", 165)]
result = race(cars)
for c in result:
 print(f"{c.license_plate}: {c.travelled_distance:.1f} km, speed {c.current_speed} km/h")
