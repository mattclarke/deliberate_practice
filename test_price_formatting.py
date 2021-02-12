from cart import Cart
from catalogue import Catalogue


def test_get_zero_total():
    cart = Cart(Catalogue())

    total = cart.get_formatted_total()

    assert total == "$0.00"


def test_non_zero_low_total():
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 123)
    cart = Cart(catalogue)

    cart.add_item_by_barcode("12345")

    assert cart.get_formatted_total() == "$1.23"


def test_non_zero_high_total():
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 123456789)
    cart = Cart(catalogue)

    cart.add_item_by_barcode("12345")

    assert cart.get_formatted_total() == "$1,234,567.89"
