import pytest

from cart import Cart, InvalidOperation
from catalogue import Catalogue


def test_can_sell_same_items_multiple_times():
    some_barcode = "12345"
    catalogue = Catalogue()
    catalogue.add_new_product(some_barcode, 123)
    cart = Cart(catalogue)

    cart.add_item_by_barcode(some_barcode)
    cart.add_item_by_barcode(some_barcode)

    assert cart.total_in_cents() == 246


def test_can_sell_different_items():
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 123)
    catalogue.add_new_product("67890", 500)
    catalogue.add_new_product("54321", 300)
    cart = Cart(catalogue)

    cart.add_item_by_barcode("67890")
    cart.add_item_by_barcode("54321")

    assert cart.total_in_cents() == 800


def test_can_add_multiples_of_item_to_cart():
    item_price = 123
    catalogue = Catalogue()
    catalogue.add_new_product("12345", item_price)
    cart = Cart(catalogue)

    multiples_of_item = 2
    cart.add_item_by_barcode("12345", multiple=multiples_of_item)

    assert cart.total_in_cents() == multiples_of_item * item_price


def test_cannot_add_fewer_than_one_item_to_cart():
    item_price = 123
    catalogue = Catalogue()
    catalogue.add_new_product("12345", item_price)
    cart = Cart(catalogue)

    with pytest.raises(InvalidOperation):
        cart.add_item_by_barcode("12345", multiple=0)
