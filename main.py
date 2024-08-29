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
