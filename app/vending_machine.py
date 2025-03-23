from enum import Enum
from typing import Self


class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUATER = 25


class VendingMachine:
    amount: int = 0

    def insert_coin(self, coin: Coin) -> Self:
        self.amount = self.amount + coin.value
        return self

    def current_amount(self) -> int:
        return self.amount
