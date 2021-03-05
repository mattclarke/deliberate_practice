from catalogue import Catalogue
import locale

from exceptions import UnknownBarcode, InvalidOperation
from tax_rate import TAX_MULTIPLIER


def format_total(total_in_cents: int) -> str:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    total_in_dollars = total_in_cents / 100
    return locale.currency(total_in_dollars, grouping=True)


class Cart:
    def __init__(self, items: Catalogue):
        self._items = items
        self._total = 0

    def add_item_by_barcode(self, barcode: str, multiple: int = 1):
        if multiple < 1:
            raise InvalidOperation("Must add 1 or more items to cart")
        try:
            self._total += self._items.get_price(barcode) * multiple
        except KeyError:
            raise UnknownBarcode(f"Unknown barcode '{barcode}'")

    def total_in_cents(self) -> int:
        return self._total

    def finish_sale(self):
        self._total = 0

    def total_with_tax(self):
        return self.total_in_cents() * TAX_MULTIPLIER
