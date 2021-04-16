from typing import Dict, Tuple
from dataclasses import dataclass, astuple


@dataclass
class Item:
    price: int
    taxable: bool


class Catalogue:
    def __init__(self):
        self._items: Dict[str, Item] = {}

    def add_new_product(self, barcode: str, price: int, is_taxable: bool = False):
        self._items[barcode] = Item(price, is_taxable)

    def contains(self, barcode: str):
        return barcode in self._items

    def get_price(self, barcode: str) -> Tuple[int, bool]:
        return astuple(self._items[barcode])  # type: ignore
