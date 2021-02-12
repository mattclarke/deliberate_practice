from catalogue import Catalogue
from cart import Cart

command_total = "total"

if __name__ == "__main__":
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 345)
    catalogue.add_new_product("23473", 273)

    system = Cart(catalogue)

    while True:
        command = input(">")
        if command == command_total:
            print(f"total = {system.calculate_total()}")
            break

        system.add_item_by_barcode(command)
