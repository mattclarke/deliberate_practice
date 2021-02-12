from catalogue import Catalogue
from cart import Cart

if __name__ == "__main__":
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 345)

    system = Cart(catalogue)

    while True:
        command = input(">")
        if command == "total":
            print(f"total = {system.calculate_total()}")
            break

        system.add_item_by_barcode(command)
