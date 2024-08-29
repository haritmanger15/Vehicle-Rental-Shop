class Vehicle:
    # Class variable to keep track of the last assigned ID
    last_id = 0

    def __init__(self, type, daily_rate, weekly_rate, stock):
        # Increment the last_id for each new vehicle created
        Vehicle.last_id += 1
        self.id = f"V{Vehicle.last_id:03d}"  # Generate a unique ID in the format V001, V002, etc.
        self.type = type  # Type of the vehicle (e.g., compact car, sedan, SUV)
        self.daily_rate = daily_rate  # Daily rental rate for the vehicle
        self.weekly_rate = weekly_rate  # Weekly rental rate for the vehicle
        self.stock = stock  # Number of available units of this vehicle type
