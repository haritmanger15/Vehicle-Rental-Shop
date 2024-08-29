class Customer:
    def __init__(self, name):
        # Initialize the Customer with their name and no rented vehicle
        self.name = name  # Customer's name
        self.rented_vehicle = None  # Initially, no vehicle is rented

    def rent_vehicle(self, rental_shop, vehicle_type, days):
        # Attempt to rent a vehicle of the specified type for a given number of days
        vehicle = next((v for v in rental_shop.vehicles if v.type.lower() == vehicle_type.lower() and v.stock > 0), None)

        if vehicle:
            if rental_shop.rent_vehicle(vehicle):  # Try to rent the vehicle through the rental shop
                self.rented_vehicle = {'vehicle': vehicle, 'days': days}  # Store the rented vehicle and rental period
                daily_rate = vehicle.daily_rate  # Get the daily rental rate
                total_payment = daily_rate * days  # Calculate total payment
                
                # Return an invoice detailing the rental transaction
                return (f" ========================================\n"
                        f"                 INVOICE                  \n"
                        f" ========================================\n"
                        f" Customer Name: {self.name}\n"
                        f" Vehicle Type: {vehicle.type}\n"
                        f" Rental Period: {days} days\n"
                        f" Daily Rate: ${daily_rate}\n"
                        f" ----------------------------------------\n"
                        f" Total Payment: ${total_payment}\n"
                        f" ========================================\n")
            else:
                return f"Sorry, {vehicle_type}s are currently out of stock."  # Vehicle not available for rent
        else:
            return f"Sorry, {vehicle_type}s are currently out of stock."  # No matching vehicle found

    def return_vehicle(self, rental_shop):
        # Handle the return of a rented vehicle
        if self.rented_vehicle:
            vehicle = self.rented_vehicle['vehicle']  # Get the rented vehicle
            days = self.rented_vehicle['days']  # Get the rental period
            rental_shop.return_vehicle(vehicle)  # Return the vehicle to the rental shop

            daily_rate = vehicle.daily_rate  # Get the daily rental rate
            total_payment = daily_rate * days  # Calculate total payment
            self.rented_vehicle = None  # Clear the rented vehicle information

            # Return an invoice detailing the rental transaction
            return (f" ========================================\n"
                    f"                 INVOICE                  \n"
                    f" ========================================\n"
                    f" Customer Name: {self.name}\n"
                    f" Vehicle Type: {vehicle.type}\n"
                    f" Rental Period: {days} days\n"
                    f" Daily Rate: ${daily_rate}\n"
                    f" ----------------------------------------\n"
                    f" Total Payment: ${total_payment}\n"
                    f" ========================================\n")
        else:
            return "No vehicle to return."  # No vehicle has been rented

    def inquire_inventory(self, rental_shop):
        # Inquire about the rental shop's inventory
        inventory_data = [
            [v.type, f"${v.daily_rate}", f"${v.weekly_rate}", v.stock]  # Show stock as a numerical value
            for v in rental_shop.vehicles  # Create a list of vehicle types, rates, and availability
        ]
        return inventory_data  # Return the compiled inventory data

    def inquire_prices(self, rental_shop):
        # Inquire about the prices of vehicles in the rental shop
        prices_data = []
        for vehicle in rental_shop.vehicles:
            # Append vehicle type and its corresponding daily and weekly rates to the prices_data list
            prices_data.append([vehicle.type, f"${vehicle.daily_rate}", f"${vehicle.weekly_rate}"])
        return prices_data  # Return the compiled prices data
