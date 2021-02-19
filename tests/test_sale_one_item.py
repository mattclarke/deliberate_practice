from catalogue import Catalogue
from cart import Cart, UnknownBarcode


def create_catalogue():
    catalogue = Catalogue()
    catalogue.add_new_product("1234567890", 1234)
    catalogue.add_new_product("42424242", 42)
    return catalogue


def test_can_add_one_item_and_retrieve_its_price_as_the_total():
    cart = Cart(create_catalogue())

    cart.add_item_by_barcode("1234567890")

    assert cart.total_in_cents() == 1234


def test_can_add_a_different_item_and_retrieve_its_price_as_the_total():
    cart = Cart(create_catalogue())

    cart.add_item_by_barcode("42424242")

    assert cart.total_in_cents() == 42


def test_adding_unknown_barcode_raises_exception():
    cart = Cart(create_catalogue())

    try:
        cart.add_item_by_barcode("unknown")
    except UnknownBarcode:
        pass
