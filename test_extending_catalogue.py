
def test_can_add_new_item_to_catalogue():
    catalogue = Catalogue()

    catalogue.add_new_product("product1", 6789)

    assert "product1" in catalogue
    assert catalogue["product1"] == 6789
