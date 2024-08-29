from customer import Customer  # Ensure this import statement is at the top

class VIPCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)

    def get_vip_daily_rate(self, vehicle_type):
        # Centralize VIP rate determination
        vip_rates = {
            "compact car": 10,
            "sedan": 30,
            "SUV": 70
        }
        return vip_rates.get(vehicle_type, None)  # Use VIP rate or None if vehicle type is not found

    def rent_vehicle(self, rental_shop, vehicle_type, days):
        # Override to apply VIP pricing when renting a vehicle
        vehicle = next((v for v in rental_shop.vehicles if v.type.lower() == vehicle_type.lower() and v.stock > 0), None)

        if vehicle:
            if rental_shop.rent_vehicle(vehicle):
                self.rented_vehicle = {'vehicle': vehicle, 'days': days}
                vip_daily_rate = self.get_vip_daily_rate(vehicle.type)
                daily_rate = vip_daily_rate if vip_daily_rate is not None else vehicle.daily_rate
                total_payment = daily_rate * days

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
                return f"Sorry, {vehicle_type}s are currently out of stock."
        else:
            return f"Sorry, {vehicle_type}s are currently out of stock."

    def return_vehicle(self, rental_shop):
        # Apply the same VIP pricing when returning the vehicle
        if self.rented_vehicle:
            vehicle = self.rented_vehicle['vehicle']
            days = self.rented_vehicle['days']
            rental_shop.return_vehicle(vehicle)

            vip_daily_rate = self.get_vip_daily_rate(vehicle.type)
            daily_rate = vip_daily_rate if vip_daily_rate is not None else vehicle.daily_rate
            total_payment = daily_rate * days
            self.rented_vehicle = None

            return (f" ========================================\n"
                    f"                 INVOICE                 \n"
                    f" ========================================\n"
                    f" Customer Name: {self.name}\n"
                    f" Vehicle Type: {vehicle.type}\n"
                    f" Rental Period: {days} days\n"
                    f" Daily Rate: ${daily_rate}\n"
                    f" ----------------------------------------\n"
                    f" Total Payment: ${total_payment}\n"
                    f" ========================================\n")
        else:
            return "No vehicle to return."
