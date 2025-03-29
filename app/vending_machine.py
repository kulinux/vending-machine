from enum import Enum
from typing import Callable, Optional, Self
from dataclasses import dataclass
from app.model import Money, Coin, Product
from app.inventory import Inventory



class VendingMachine:
    __amount: Money
    __display: Callable[[str], None]
    __inventory: Inventory

    def __init__(self, amount: Money, display: Callable[[str], None], inventory: Inventory):
        self.__amount = amount
        self.__display = display
        self.__inventory = inventory
        self.__display("INSERT COIN")

    def insert_coin(self, coin: Coin) -> Self:
        new_amount = self.__amount + coin.value

        self.__display("Total: " + str(new_amount))

        return self.__copy(new_amount)

    def current_amount(self) -> Money:
        return self.__amount

    def select(self, product: Product) -> tuple[Self, Optional[Product], Money]:
        if self.__inventory.get_item(product) is None:
            self.__display("SOLD OUT")
            self.__display("")
            return (self, None, Money.zero())

        if product.value <= self.__amount:
            change = self.__amount - product.value
            self.__display("THANK YOU")
            self.__display("")
            return (self.__copy(Money.zero()), product, change)
        else:
            self.__display("PRICE " + str(product.value))
            self.__display(str(self.__amount))
            return (self, None, Money.zero())

    def __copy(self, amount: Money):
        return self.__class__(amount, self.__display, self.__inventory)

    @staticmethod
    def newInstance(
        display: Callable[[str], None] = lambda _: None,
        inventory: Inventory = None,
    ) -> "VendingMachine":
        return VendingMachine(Money.zero(), display, inventory or Inventory())
