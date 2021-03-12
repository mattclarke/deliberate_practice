from catalogue import Catalogue


def test_can_add_new_item_to_catalogue():
    catalogue = Catalogue()

    catalogue.add_new_product("product1", 6789)

    assert catalogue.contains("product1")


def test_can_add_new_taxed_item_to_catalogue():
    catalogue = Catalogue()

    catalogue.add_new_product("product1", 6789, True)

    assert catalogue.get_price("product1") == (6789, True)


def test_catalogue_does_not_contain_item():
    empty_catalogue = Catalogue()

    assert not empty_catalogue.contains("product1")


def test_can_retrieve_item_value_when_present():
    catalogue = Catalogue()
    new_product = ("product1", 6789)

    catalogue.add_new_product(*new_product)

    assert catalogue.get_price(new_product[0])[0] == new_product[1]


def test_can_retrieve_different_item_value_when_present():
    catalogue = Catalogue()
    new_product = ("product2", 4321)

    catalogue.add_new_product(*new_product)

    assert catalogue.get_price(new_product[0])[0] == new_product[1]
