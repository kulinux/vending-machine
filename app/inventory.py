from typing import Optional, Dict
from app.model import Product

class Inventory:
    __items: Dict[Product, int] = {}

    def get_item(self, product: Product) -> Optional[Product]:
        if product in self.__items and self.__items[product] > 0:
            self.__items[product] -= 1
            return product
        return None

    def fill(self, item: tuple[int, Product]) -> None:
        quantity, product = item
        self.__items[product] = quantity