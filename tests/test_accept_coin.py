from typing import Callable
from app.vending_machine import VendingMachine, Coin
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

    display.assert_called_with("Total: 1")
