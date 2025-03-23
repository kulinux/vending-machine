from typing import Callable
from app.vending_machine import Product, VendingMachine, Coin
from unittest.mock import MagicMock


def test_when_a_valid_coin_is_inserted_add_to_current_amount():
    vending_machine = VendingMachine.newInstance()

    actual = vending_machine.insert_coin(Coin.PENNY).current_amount()

    assert actual == 1


def test_when_two_valid_coin_is_inserted_add_to_current_amount():
    vending_machine = VendingMachine.newInstance()

    actual = (
        vending_machine.insert_coin(Coin.PENNY)
        .insert_coin(Coin.NICKEL)
        .current_amount()
    )

    assert actual == 6


def test_when_a_valid_coint_is_inserted_display_will_be_updated():
    display: Callable[[str], None] = MagicMock()
    vending_machine = VendingMachine.newInstance(display)

    vending_machine.insert_coin(Coin.PENNY)

    display.assert_any_call("Total: 1")


def test_when_no_coin_display_insert_coin():
    display: Callable[[str], None] = MagicMock()
    VendingMachine.newInstance(display)

    display.assert_called_with("INSERT COIN")


def test_should_select_product():
    vending_machine = VendingMachine.newInstance()

    (_, product) = (
        vending_machine.insert_coin(Coin.QUATER)
        .insert_coin(Coin.QUATER)
        .select(Product.CHIPS)
    )

    assert product == Product.CHIPS


def test_should_display_thank_you_when_select_product():
    display: Callable[[str], None] = MagicMock()
    vending_machine = VendingMachine.newInstance(display)

    vending_machine.insert_coin(Coin.QUATER).insert_coin(Coin.QUATER).select(
        Product.CHIPS
    )

    display.assert_any_call("THANK YOU")
    display.assert_any_call("")


def test_should_amount_to_zero_after_select():
    vending_machine = VendingMachine.newInstance()

    (vm, _) = (
        vending_machine.insert_coin(Coin.QUATER)
        .insert_coin(Coin.QUATER)
        .select(Product.CHIPS)
    )

    assert vm.current_amount() == 0


def test_when_no_enough_money_display_price_of_the_item():
    display: Callable[[str], None] = MagicMock()
    vending_machine = VendingMachine.newInstance(display)

    (_, product) = vending_machine.insert_coin(Coin.PENNY).select(Product.CHIPS)

    display.assert_any_call("PRICE 50")
    display.assert_any_call("1")

    assert product is None
