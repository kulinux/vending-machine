from enum import Enum
from typing import Callable, Optional, Self
from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    cents: int

    def __add__(self, other: 'Money') -> 'Money':
        return Money(self.cents + other.cents)

    def __sub__(self, other: 'Money') -> 'Money':
        return Money(self.cents - other.cents)

    def __le__(self, other: 'Money') -> bool:
        return self.cents <= other.cents

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents

    def __str__(self) -> str:
        return str(self.cents)

    @staticmethod
    def zero() -> 'Money':
        return Money(0)

class Coin(Enum):
    PENNY = Money(1)
    NICKEL = Money(5)
    DIME = Money(10)
    QUATER = Money(25)

class Product(Enum):
    COLA = Money(100)
    CHIPS = Money(50)
    CANDY = Money(65)

