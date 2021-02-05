from catalogue import Catalogue


def test_can_add_new_item_to_catalogue():
    catalogue = Catalogue()

    catalogue.add_new_product("product1", 6789)

    assert catalogue.contains("product1")


def test_catalogue_doesnt_contain_item():
    empty_catalogue = Catalogue()

    assert not empty_catalogue.contains("product1")
