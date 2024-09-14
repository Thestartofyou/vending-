import csv
from datetime import datetime

# File to store data
CSV_FILE = 'vending_machine_data.csv'

# Sample inventory for a vending machine (product: quantity)
inventory = {
    "soda": 20,
    "chips": 15,
    "candy": 25
}

# Prices for each product (product: price)
prices = {
    "soda": 1.50,
    "chips": 1.00,
    "candy": 0.75
}

# Function to initialize CSV if not created
def initialize_csv():
    try:
        with open(CSV_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Machine ID", "Product", "Quantity Sold", "Price per Unit", "Total Sales", "Inventory After Sale", "Date"])
    except FileExistsError:
        pass

# Function to log sales to the CSV file
def log_sale(machine_id, product, quantity_sold):
    if product not in inventory:
        print(f"Error: {product} is not available in the inventory.")
        return
    
    if inventory[product] < quantity_sold:
        print(f"Error: Not enough {product} in stock.")
        return
    
    total_sales = prices[product] * quantity_sold
    inventory[product] -= quantity_sold  # Update inventory

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([machine_id, product, quantity_sold, prices[product], total_sales, inventory[product], datetime.now()])

    print(f"Sale recorded: {quantity_sold} x {product} sold from machine {machine_id}.")

# Example: Record a sale
def record_sale():
    machine_id = input("Enter Machine ID: ")
    product = input("Enter Product Sold (soda/chips/candy): ").lower()
    quantity_sold = int(input("Enter Quantity Sold: "))
    
    log_sale(machine_id, product, quantity_sold)

# Run script
if __name__ == "__main__":
    initialize_csv()
    record_sale()
