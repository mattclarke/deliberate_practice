from cart import Cart
from catalogue import Catalogue


def test_can_sell_same_items_multiple_times():
    some_barcode = "12345"
    catalogue = Catalogue()
    catalogue.add_new_product(some_barcode, 123)
    cart = Cart(catalogue)

    cart.add_item_by_barcode(some_barcode)
    cart.add_item_by_barcode(some_barcode)

    assert cart.calculate_total() == 246


def test_can_sell_different_items():
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 123)
    catalogue.add_new_product("67890", 500)
    catalogue.add_new_product("54321", 300)
    cart = Cart(catalogue)

    cart.add_item_by_barcode("67890")
    cart.add_item_by_barcode("54321")

    assert cart.calculate_total() == 800
