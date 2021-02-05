from typing import Dict


class Catalogue:
    def __init__(self):
        self._items: Dict[str, int] = {}

    def add_new_product(self, barcode: str, price: int):
        self._items[barcode] = price

    def contains(self, barcode: str):
        return barcode in self._items

    def get_price(self, barcode: str) -> int:
        return self._items[barcode]
