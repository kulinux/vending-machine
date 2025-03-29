from app.inventory import Inventory
from app.model import Product


def test_when_no_inventory_return_none():
    inventory = Inventory()
    assert inventory.get_item(Product.CHIPS) is None

def test_when_inventory_has_item_return_item():
    inventory = Inventory()
    inventory.fill((1, Product.CHIPS))
    assert inventory.get_item(Product.CHIPS) is Product.CHIPS

def test_when_run_out_of_item_return_none():
    inventory = Inventory()
    inventory.fill((1, Product.CHIPS))
    inventory.get_item(Product.CHIPS)
    assert inventory.get_item(Product.CHIPS) is None
