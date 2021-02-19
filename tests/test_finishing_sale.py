from cart import Cart
from catalogue import Catalogue


def test_after_finish_sale_cart_is_cleared():
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 123)
    catalogue.add_new_product("67890", 500)
    catalogue.add_new_product("54321", 300)

    cart = Cart(catalogue)
    cart.add_item_by_barcode("12345")

    cart.finish_sale()

    assert cart.total_in_cents() == 0
