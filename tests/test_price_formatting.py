from cart import Cart, format_total
from catalogue import Catalogue


def test_get_zero_total():
    cart = Cart(Catalogue())

    total = format_total(cart.total_in_cents())

    assert total == "$0.00"


def test_non_zero_low_total():
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 123)
    cart = Cart(catalogue)

    cart.add_item_by_barcode("12345")

    assert format_total(cart.total_in_cents()) == "$1.23"


def test_non_zero_high_total():
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 123456789)
    cart = Cart(catalogue)

    cart.add_item_by_barcode("12345")

    assert format_total(cart.total_in_cents()) == "$1,234,567.89"
