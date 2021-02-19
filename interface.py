from catalogue import Catalogue
from cart import Cart, format_total
from command_parsing import COMMAND_TOTAL, COMMAND_FINISH

if __name__ == "__main__":
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 345)
    catalogue.add_new_product("23473", 273)

    system = Cart(catalogue)

    while True:
        command = input(">")
        if command == COMMAND_TOTAL:
            print(f"total = {format_total(system.total_in_cents())}")
        elif command == COMMAND_FINISH:
            system.finish_sale()
        else:
            system.add_item_by_barcode(
                command.split(" ")[0], int(command.split(" ")[1])
            )
