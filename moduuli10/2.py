class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, floor):

        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            elif self.current_floor > floor:
                self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [
            Elevator(top_floor, bottom_floor)
            for _ in range(num_elevators)
        ]

    def run_elevator(self, elevator_number, destination_floor):

        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number!")
            return
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)
