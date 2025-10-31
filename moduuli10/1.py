class Elevator:
    def __init__(self, bottom_floor, top_floor):
        """Initialize the elevator with bottom and top floor numbers."""
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Elevator starts at the bottom floor
        print(f"Elevator initialized at floor {self.current_floor}.")

    def floor_up(self):
        """Move the elevator up by one floor if possible."""
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}.")
        else:
            print("Elevator is already at the top floor!")

    def floor_down(self):
        """Move the elevator down by one floor if possible."""
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}.")
        else:
            print("Elevator is already at the bottom floor!")

    def go_to_floor(self, target_floor):
        """Move the elevator to a specific floor."""
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor!")
            return

        print(f"Moving elevator from floor {self.current_floor} to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator arrived at floor {self.current_floor}.")


# Test the Elevator class directly (no main function)
h = Elevator(1, 10)

# Move to the 5th floor
h.go_to_floor(5)

# Move back down to the bottom floor
h.go_to_floor(1)
