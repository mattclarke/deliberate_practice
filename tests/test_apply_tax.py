from cart import Cart
from catalogue import Catalogue
from tax_rate import TAX_MULTIPLIER


def test_taxable_items_have_tax_applied():
    catalogue = Catalogue()
    price = 1234
    barcode = "12345"
    catalogue.add_new_product(barcode, price, is_taxable=True)
    cart = Cart(catalogue)
    cart.add_item_by_barcode(barcode)

    assert cart.gross_total() == price * TAX_MULTIPLIER


def test_non_taxable_items_do_not_have_tax_applied():
    catalogue = Catalogue()
    price = 1234
    barcode = "12345"
    catalogue.add_new_product(barcode, price, is_taxable=False)
    cart = Cart(catalogue)
    cart.add_item_by_barcode(barcode)

    assert cart.gross_total() == price


def test_multiple_items_some_taxed_some_not_taxed():
    catalogue = Catalogue()

    items = (
        ("12345", 1234, True, 1),
        ("34956", 3273, False, 3),
        ("682475", 234, True, 2),
    )
    cart = Cart(catalogue)
    for barcode, price, taxable, quantity in items:
        catalogue.add_new_product(barcode, price, taxable)
        cart.add_item_by_barcode(barcode, quantity)

    contribution_from_item_1 = 1234 * TAX_MULTIPLIER
    contribution_from_item_2 = 3273 * 3
    contribution_from_item_3 = 234 * TAX_MULTIPLIER * 2
    assert (
        cart.gross_total()
        == contribution_from_item_1
        + contribution_from_item_2
        + contribution_from_item_3
    )
