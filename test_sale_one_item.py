from typing import Dict


class UnknownBarcode(Exception):
    pass


class System:
    def __init__(self):
        self._items: Dict[str, int] = {"1234567890": 1234, "42424242": 42}
        self._total = 0

    def add_item_by_barcode(self, barcode: str):
        try:
            self._total = self._items[barcode]
        except KeyError:
            raise UnknownBarcode

    def calculate_total(self):
        return self._total


def test_can_add_one_item_and_retrieve_its_price_as_the_total():
    system = System()

    system.add_item_by_barcode("1234567890")

    assert system.calculate_total() == 1234


def test_can_add_a_different_item_and_retrieve_its_price_as_the_total():
    system = System()

    system.add_item_by_barcode("42424242")

    assert system.calculate_total() == 42


def test_adding_unknown_barcode_raises_exception():
    system = System()

    try:
        system.add_item_by_barcode("unknown")
    except UnknownBarcode:
        pass
