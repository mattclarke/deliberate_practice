from catalogue import Catalogue
from cart import Cart
from exceptions import UnknownBarcode


def create_catalogue():
    catalogue = Catalogue()
    catalogue.add_new_product("1234567890", 1234)
    catalogue.add_new_product("42424242", 42)
    return catalogue


def test_can_add_one_item_and_retrieve_its_price_as_the_total():
    cart = Cart(create_catalogue())

    cart.add_item_by_barcode("1234567890")

    assert cart.net_total() == 1234


def test_can_add_a_different_item_and_retrieve_its_price_as_the_total():
    cart = Cart(create_catalogue())

    cart.add_item_by_barcode("42424242")

    assert cart.net_total() == 42


def test_adding_unknown_barcode_raises_exception():
    cart = Cart(create_catalogue())

    try:
        cart.add_item_by_barcode("unknown")
    except UnknownBarcode:
        pass


def test_get_items_in_empty_basket():
    cart = Cart(create_catalogue())

    assert not cart.get_items()


def test_get_items_in_basket_with_one_item():
    cart = Cart(create_catalogue())
    barcode_scanned = "42424242"
    cart.add_item_by_barcode(barcode_scanned)

    items = cart.get_items()

    assert len(items) == 1
    assert barcode_scanned in items[0]
