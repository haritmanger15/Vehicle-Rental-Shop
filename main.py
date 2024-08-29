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

from vehicle import Vehicle
from customer import Customer
from vip_customer import VIPCustomer
from rental_shop import RentalShop
from tabulate import tabulate

# Function to print data in a tabular format
def print_table(data, headers):
    table = tabulate(data, headers=headers, tablefmt="grid")  # Create a formatted table
    print(table)  # Print the table to the console

# Main function to run the rental shop application
def main():
    # Create vehicles with stock levels
    vehicles = [
        Vehicle("compact car", 20, 15, 5),
        Vehicle("sedan", 40, 35, 3),
        Vehicle("SUV", 80, 70, 2)
    ]
    
    rental_shop = RentalShop(vehicles)

    # Get customer type and name
    customer_type = input("Are you a VIP customer? (yes/no): ").strip().lower()
    customer_name = input("Enter your name: ")

    # Create a Customer or VIPCustomer instance based on user input
    customer = VIPCustomer(customer_name) if customer_type == "yes" else Customer(customer_name)

    # Main loop for customer actions
    while True:
        # Prompt user for action with numbered options
        print("\nWhat would you like to choose?")
        print("1. Rent")
        print("2. Return")
        print("3. Inquire")
        print("4. Exit")
        
        action = input("Please enter the number corresponding to your choice: ").strip()

        # Handle renting a vehicle
        if action == "1":
            # Prompt the user to select a vehicle type
            print("Select the type of vehicle you'd like to rent:")
            print("1. Compact Car")
            print("2. Sedan")
            print("3. SUV")
            
            vehicle_choice = input("Enter the number corresponding to your choice: ").strip()
            if vehicle_choice == "1":
                vehicle_type = "compact car"
            elif vehicle_choice == "2":
                vehicle_type = "sedan"
            elif vehicle_choice == "3":
                vehicle_type = "SUV"
            else:
                print("Invalid vehicle type selected. Please try again.")
                continue
            
            days = int(input("Enter the number of days: "))  # Get number of rental days
            result = customer.rent_vehicle(rental_shop, vehicle_type, days)  # Attempt to rent vehicle
            print(result)  # Print the result of the rental attempt

        # Handle returning a vehicle
        elif action == "2":
            result = customer.return_vehicle(rental_shop)  # Attempt to return vehicle
            print(result)  # Print the result of the return attempt

        # Handle inventory and pricing inquiries
        elif action == "3":
            # Inquire about inventory and print it in table format
            inventory_data = customer.inquire_inventory(rental_shop)
            print_table(inventory_data, ["Type", "Daily Rate", "Weekly Rate", "Available Stock"])  # Print inventory

            # Inquire about prices and print them in table format
            prices_data = customer.inquire_prices(rental_shop)
            print_table(prices_data, ["Type", "Daily Rate", "Weekly Rate"])  # Print prices

        # Exit the application
        elif action == "4":
            print("Thank you for using the car rental service. Goodbye!")
            break  # Exit the loop and end the program

        # Handle invalid actions
        else:
            print("Invalid action. Please try again.")  # Prompt for valid action

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the application
