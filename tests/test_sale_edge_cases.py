from cart import Cart
from exceptions import UnknownBarcode
from catalogue import Catalogue


def test_get_total_with_no_items():
    catalogue = Catalogue()
    cart = Cart(catalogue)

    assert cart.total_in_cents() == 0


def test_total_remains_same_after_unknown_barcode():
    catalogue = Catalogue()
    cart = Cart(catalogue)

    try:
        cart.add_item_by_barcode("unknown")
    except UnknownBarcode:
        pass

    assert cart.total_in_cents() == 0
