from typing import List


class Catalogue:
    def __init__(self):
        self._items: List[str] = []

    def add_new_product(self, barcode: str, price: int):
        self._items.append(barcode)

    def contains(self, barcode: str):
        return barcode in self._items
