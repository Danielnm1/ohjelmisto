class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):

        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):

        self.travelled_distance += self.current_speed * hours

    def print_information(self):
        print(f"Car registration number: {self.license_plate}")
        print(f"Maximum speed: {self.maximum_speed} km/h")
        print(f"Current speed: {self.current_speed} km/h")
        print(f"Travelled distance: {self.travelled_distance} km")


class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity

    def print_information(self):
        super().print_information()
        print(f"Battery capacity: {self.battery_capacity} kWh")


class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume

    def print_information(self):
        super().print_information()
        print(f"Tank volume: {self.tank_volume} liters")
auto =ElectricCar("ABC-15", 180 , 52.5)
auto.print_information()