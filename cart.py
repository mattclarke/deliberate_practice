from catalogue import Catalogue
import locale


class Cart:
    def __init__(self, items: Catalogue):
        self._items = items
        self._total = 0
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    def add_item_by_barcode(self, barcode: str):
        try:
            self._total += self._items.get_price(barcode)
        except KeyError:
            raise UnknownBarcode

    def total_in_cents(self) -> int:
        return self._total

    def get_formatted_total(self):
        # TODO smell: this belongs somewhere else?
        total_in_dollars = self._total / 100
        return locale.currency(total_in_dollars, grouping=True)


class UnknownBarcode(Exception):
    pass
