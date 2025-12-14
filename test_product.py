import pytest
from product import get_product_details

def test_get_product_details():
    name = "Laptop"
    prod_id = "PROD2020"
    quantity = 1
    price = 60000

    expected_output = (
        "Product Name: Laptop\n"
        "Product ID: PROD2020\n"
        "Quantity: 1\n"
        "Price: 60,000"
    )

    assert get_product_details(name, prod_id, quantity, price) == expected_output
