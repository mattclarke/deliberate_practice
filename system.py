from typing import Dict


class System:
    def __init__(self, items):
        self._items: Dict[str, int] = items
        self._total = 0

    def add_item_by_barcode(self, barcode: str):
        try:
            self._total = self._items[barcode]
        except KeyError:
            raise UnknownBarcode

    def calculate_total(self):
        return self._total


class UnknownBarcode(Exception):
    pass
