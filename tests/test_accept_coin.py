from typing import Callable
from app.vending_machine import Product, VendingMachine, Coin, Money, Inventory
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def display():
    return MagicMock(spec=Callable[[str], None])

@pytest.fixture
def inventory():
    inventory = MagicMock(spec=Inventory)
    inventory.get_item.return_value = Product.CHIPS
    return inventory

def test_when_a_valid_coin_is_inserted_add_to_current_amount(inventory):
    vending_machine = VendingMachine.newInstance(inventory=inventory)

    actual = vending_machine.insert_coin(Coin.PENNY).current_amount()

    assert actual == Money(1)


def test_when_two_valid_coin_is_inserted_add_to_current_amount(inventory):
    vending_machine = VendingMachine.newInstance(inventory=inventory)

    actual = (
        vending_machine.insert_coin(Coin.PENNY)
        .insert_coin(Coin.NICKEL)
        .current_amount()
    )

    assert actual == Money(6)


def test_when_a_valid_coint_is_inserted_display_will_be_updated(display, inventory):
    vending_machine = VendingMachine.newInstance(display, inventory)

    vending_machine.insert_coin(Coin.PENNY)

    display.assert_any_call("Total: 1")


def test_when_no_coin_display_insert_coin(display, inventory):
    VendingMachine.newInstance(display, inventory)

    display.assert_called_with("INSERT COIN")


def test_should_select_product(inventory):
    vending_machine = VendingMachine.newInstance(inventory=inventory)

    (_, product, _) = (
        vending_machine.insert_coin(Coin.QUATER)
        .insert_coin(Coin.QUATER)
        .select(Product.CHIPS)
    )

    assert product == Product.CHIPS


def test_should_display_thank_you_when_select_product(display, inventory):
    vending_machine = VendingMachine.newInstance(display, inventory)

    vending_machine.insert_coin(Coin.QUATER).insert_coin(Coin.QUATER).select(
        Product.CHIPS
    )

    display.assert_any_call("THANK YOU")
    display.assert_any_call("")


def test_should_amount_to_zero_after_select(inventory):
    vending_machine = VendingMachine.newInstance(inventory=inventory)

    (vm, _, _) = (
        vending_machine.insert_coin(Coin.QUATER)
        .insert_coin(Coin.QUATER)
        .select(Product.CHIPS)
    )

    assert vm.current_amount() == Money.zero()


def test_when_no_enough_money_display_price_of_the_item(display, inventory):
    vending_machine = VendingMachine.newInstance(display, inventory)

    (_, product, _) = vending_machine.insert_coin(Coin.PENNY).select(Product.CHIPS)

    display.assert_any_call("PRICE 50")
    display.assert_any_call("1")

    assert product is None


def test_when_more_money_than_product_return_change(display, inventory):
    vending_machine = VendingMachine.newInstance(display, inventory)

    (_, _, returned_change) = (
        vending_machine.insert_coin(Coin.QUATER)
        .insert_coin(Coin.QUATER)
        .insert_coin(Coin.QUATER)
        .select(Product.CHIPS)
    )

    assert returned_change == Money(25)


def test_should_display_sold_out_when_no_items_left(display):
    inventory: Inventory = MagicMock()
    inventory.get_item.return_value = None

    vending_machine = VendingMachine.newInstance(display, inventory)

    vending_machine.insert_coin(Coin.QUATER).insert_coin(Coin.QUATER).select(
        Product.CHIPS
    )

    inventory.get_item.assert_called_with(Product.CHIPS)
    display.assert_any_call("SOLD OUT")
    display.assert_any_call("")
    
    
