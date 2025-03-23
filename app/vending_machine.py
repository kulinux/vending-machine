from enum import Enum
from typing import Callable, Optional, Self


class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUATER = 25


class Product(Enum):
    COLA = 100
    CHIPS = 50
    CANDY = 65


class VendingMachine:
    __amount: int
    __display: Callable[[str], None]

    def __init__(self, amount: int, display: Callable[[str], None]):
        self.__amount = amount
        self.__display = display
        self.__display("INSERT COIN")

    def insert_coin(self, coin: Coin) -> Self:
        new_amount = self.__amount + coin.value

        self.__display("Total: " + str(new_amount))

        return self.__copy(new_amount)

    def current_amount(self) -> int:
        return self.__amount

    def select(self, product: Product) -> tuple[Self, Optional[Product]]:
        if product.value <= self.__amount:
            self.__display("THANK YOU")
            self.__display("")
            return (self.__copy(0), product)
        else:
            self.__display("PRICE " + str(product.value))
            self.__display(str(self.__amount))
            return (self, None)

    def __copy(self, amount: int):
        return self.__class__(amount, self.__display)

    @staticmethod
    def newInstance(
        display: Callable[[str], None] = lambda _: None,
    ) -> "VendingMachine":
        return VendingMachine(0, display)
