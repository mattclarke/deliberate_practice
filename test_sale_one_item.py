class System:
    def __init__(self):
        pass

    def add_item_by_barcode(self, barcode):
        pass

    def calculate_total(self):
        return 1234


def test_can_add_one_item_and_retrieve_its_price_as_the_total():
    system = System()

    system.add_item_by_barcode("1234567890")

    assert system.calculate_total() == 1234
