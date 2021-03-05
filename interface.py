from catalogue import Catalogue
from cart import Cart
from exceptions import PointOfSaleError
from command_parsing import COMMANDS, parse_command

if __name__ == "__main__":
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 345)
    catalogue.add_new_product("23473", 273)

    system = Cart(catalogue)

    print(f"Commands are: {', '.join(COMMANDS)}")

    while True:
        command = input("> ").strip()
        if command == "quit":
            break

        try:
            response = parse_command(command, system)
            if response is not None:
                print(f"{response}")
        except PointOfSaleError as e:
            print(e)
