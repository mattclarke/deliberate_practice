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
        self._net_total = 0
        self._gross_total = 0

    def add_item_by_barcode(self, barcode: str, multiple: int = 1):
        if multiple < 1:
            raise InvalidOperation("Must add 1 or more items to cart")
        try:
            price, taxable = self._items.get_price(barcode)
            net_price = price * multiple
            self._net_total += net_price
            applicable_tax_multiplier = TAX_MULTIPLIER if taxable else 1
            self._gross_total += net_price * applicable_tax_multiplier
        except KeyError:
            raise UnknownBarcode(f"Unknown barcode '{barcode}'")

    def net_total(self) -> int:
        return self._net_total

    def gross_total(self) -> int:
        return self._gross_total

    def finish_sale(self):
        self._net_total = 0
