from cart import Cart
from catalogue import Catalogue
from tax_rate import TAX_MULTIPLIER


def test_taxable_items_have_tax_applied():
    catalogue = Catalogue()
    price = 1234
    barcode = "12345"
    catalogue.add_new_product(barcode, price)
    cart = Cart(catalogue)
    cart.add_item_by_barcode(barcode)

    assert cart.total_with_tax() == price * TAX_MULTIPLIER
