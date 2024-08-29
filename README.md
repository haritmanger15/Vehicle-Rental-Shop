# Vehicle Rental Shop

Welcome to the **Vehicle Rental Shop** application! This project simulates a car rental service where users can rent and return vehicles, inquire about inventory, and check prices. The system supports both regular customers and VIP customers, offering VIP-specific pricing.

---

## Features

- **Vehicle Rental**: Rent vehicles with daily and weekly rates.
- **Vehicle Return**: Return rented vehicles and generate an invoice.
- **Inventory Inquiry**: View available stock and rates of different vehicle types.
- **Price Inquiry**: Check daily and weekly rental rates for all vehicles.
- **VIP Pricing**: Special rates for VIP customers.

## Classes

### Vehicle
Represents a vehicle in the rental shop.
- **Attributes**:
  - `id`: Unique identifier for the vehicle.
  - `type`: Type of the vehicle (e.g., compact car, sedan, SUV).
  - `daily_rate`: Daily rental rate.
  - `weekly_rate`: Weekly rental rate.
  - `stock`: Number of available units.

### Customer
Represents a customer renting a vehicle.
- **Methods**:
  - `rent_vehicle(rental_shop, vehicle_type, days)`: Rent a vehicle of the specified type for a given number of days.
  - `return_vehicle(rental_shop)`: Return a rented vehicle.
  - `inquire_inventory(rental_shop)`: Inquire about the rental shop's inventory.
  - `inquire_prices(rental_shop)`: Inquire about the prices of vehicles.

### VIPCustomer
Inherits from `Customer`, with VIP-specific rental rates.
- **Methods**:
  - `get_vip_daily_rate(vehicle_type)`: Centralize VIP rate determination.
  - `rent_vehicle(rental_shop, vehicle_type, days)`: Rent a vehicle with VIP pricing.
  - `return_vehicle(rental_shop)`: Return a vehicle with VIP pricing.

### RentalShop
Manages the vehicle inventory and handles rentals and returns.
- **Methods**:
  - `rent_vehicle(vehicle)`: Rent out a vehicle if available.
  - `return_vehicle(vehicle)`: Return a vehicle to the inventory.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/vehicle-rental-shop.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd vehicle-rental-shop
   ```

3. **Install dependencies**:
   ```bash
   pip install tabulate
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Follow the on-screen prompts** to rent or return vehicles, inquire about inventory, or check prices.

## Sample Output

### Renting a Vehicle

```
 ========================================
                 INVOICE                  
 ========================================
 Customer Name: John Doe
 Vehicle Type: SUV
 Rental Period: 5 days
 Daily Rate: $80
 ----------------------------------------
 Total Payment: $400
 ========================================
```

### Returning a Vehicle

```
 ========================================
                 INVOICE                 
 ========================================
 Customer Name: John Doe
 Vehicle Type: SUV
 Rental Period: 5 days
 Daily Rate: $80
 ----------------------------------------
 Total Payment: $400
 ========================================
```

Certainly! Here’s a section on contributing for your `README.md` file, written in a detailed and welcoming manner:

---

## Contributing

We welcome contributions to the **Vehicle Rental Shop** project! Your involvement helps improve the project and keeps it up to date. If you want to contribute, please follow these steps:

### How to Contribute

1. **Fork the Repository**
   - Click the "Fork" button at the top right corner of this repository page to create a copy of this repository in your own GitHub account.

2. **Clone Your Fork**
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/yourusername/vehicle-rental-shop.git
     ```
   - Navigate to the project directory:
     ```bash
     cd vehicle-rental-shop
     ```

3. **Create a New Branch**
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature/your-feature-name
     ```
   - Make sure to name your branch descriptively based on the changes you plan to make.

4. **Make Your Changes**
   - Implement your feature or fix a bug. Be sure to follow the existing code style and conventions.
   - Add tests if applicable and make sure all existing and new tests pass.

5. **Commit Your Changes**
   - Stage and commit your changes with a meaningful commit message:
     ```bash
     git add .
     git commit -m "Add detailed description of your changes"
     ```

6. **Push Your Changes**
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/your-feature-name
     ```

7. **Create a Pull Request**
   - Go to the original repository on GitHub and click on "Pull Requests."
   - Click "New Pull Request" and select your branch from the dropdown menu.
   - Provide a clear description of your changes and submit the pull request.

### Pull Request Guidelines

- **Description**: Include a detailed description of the changes you’ve made and why they are necessary.
- **Code Style**: Ensure your code adheres to the project’s style guidelines.
- **Tests**: Include new tests if you are adding new features or fixing bugs, and make sure existing tests continue to pass.
- **Documentation**: Update documentation as needed to reflect your changes.

### Code of Conduct

We ask all contributors to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and respectful environment for everyone involved.

### Reporting Issues

If you find a bug or have a feature request, please open an issue on the [Issues page](https://github.com/haritmanger15/vehicle-rental-shop/issues). Provide as much detail as possible, including steps to reproduce the issue or a description of the desired feature.

Thank you for contributing to **Vehicle Rental Shop**! Your contributions are greatly appreciated.

---

Feel free to customize this section further based on your project's specific needs or guidelines.
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [haritmanger11@gmail.com](mailto:haritmanger11@gmail.com).

---

Feel free to adjust any sections according to your preferences or specific project details.
