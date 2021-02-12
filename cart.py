from catalogue import Catalogue


class Cart:
    def __init__(self, items: Catalogue):
        self._items = items
        self._total = 0

    def add_item_by_barcode(self, barcode: str):
        try:
            self._total += self._items.get_price(barcode)
        except KeyError:
            raise UnknownBarcode

    def total_in_cents(self) -> int:
        return self._total

    def get_formatted_total(self):
        return f"${self._total}"


class UnknownBarcode(Exception):
    pass
