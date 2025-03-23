from enum import Enum
from typing import Callable, Self
from dataclasses import dataclass


class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUATER = 25


class VendingMachine:
    amount: int
    display: Callable[[str], None]

    def __init__(self, amount: int, display: Callable[[str], None]):
        self.amount = amount
        self.display = display

    def insert_coin(self, coin: Coin) -> Self:
        new_amount = self.amount + coin.value

        self.display("Total: " + str(new_amount))

        copy_instance = self.__class__(new_amount, self.display)
        return copy_instance

    def current_amount(self) -> int:
        return self.amount

    @staticmethod
    def newInstance(
        display: Callable[[str], None] = lambda _: None,
    ) -> "VendingMachine":
        return VendingMachine(0, display)
