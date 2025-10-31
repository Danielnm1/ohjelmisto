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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):

        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):

        print(f"\nRace status: {self.name}")
        print("-" * 60)
        print(f"{'License Plate':<15}{'Max Speed':<12}{'Speed':<10}{'Distance (km)':<15}")
        print("-" * 60)
        for car in self.cars:
            print(
                f"{car.license_plate:<15}{car.maximum_speed:<12}{car.current_speed:<10}{car.travelled_distance:<15.1f}")
        print("-" * 60)

    def race_finished(self):

        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False



