class RentalShop:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def rent_vehicle(self, vehicle):
        if vehicle.stock > 0:  # Check if the vehicle is available (stock > 0)
            vehicle.stock -= 1  # Decrease the stock by 1 to reflect the rental
            return True  # Return True indicating the rental was successful
        else:
            return False  # Return False indicating the vehicle is not available for rent

    def return_vehicle(self, vehicle):
        vehicle.stock += 1  # Increase the stock by 1 to reflect the return
