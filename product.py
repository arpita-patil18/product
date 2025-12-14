def get_product_details(name, prod_id, quantity, price):
    return (
        f"Product Name: {name}\n"
        f"Product ID: {prod_id}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price:,}"
    )

if __name__ == "__main__":
    print(get_product_details("Laptop", "PROD00145", 1, 65000))
