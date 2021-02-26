from typing import Optional, List

from cart import Cart, format_total

COMMAND_FINISH = "finish"
COMMAND_TOTAL = "total"
COMMAND_SCAN = "scan"


class UnrecognisedCommand(Exception):
    pass


class MalformedCommand(Exception):
    pass


def parse_command(command_input: str, cart: Cart) -> Optional[str]:
    split_command = command_input.split(" ")
    command = split_command[0]

    # TODO: Tidy this
    if command == COMMAND_TOTAL:
        if len(split_command) != 1:
            raise MalformedCommand(
                f"'{command}' is malformed as it does not take parameters"
            )
        return format_total(cart.total_in_cents())
    elif command == COMMAND_FINISH:
        if len(split_command) != 1:
            raise MalformedCommand(
                f"'{command}' is malformed as it does not take parameters"
            )
        cart.finish_sale()
    elif command == COMMAND_SCAN:
        if len(split_command) > 3:
            raise MalformedCommand(
                f"'{command}' is malformed, should be of form: barcode quantity"
            )
        try:
            cart.add_item_by_barcode(split_command[1], int(split_command[2]))
        except IndexError:
            raise MalformedCommand(
                f"'{command}' is malformed, should be of form: barcode quantity"
            )
    else:
        raise UnrecognisedCommand(f"'{command}' is not a recognised command")
    return None


def _get_barcode_and_quantity(command: str, split_command: List[str]):
    try:
        barcode = split_command[1]
        quantity = int(split_command[2])
    except IndexError:
        raise MalformedCommand(
            f"'{command}' is malformed, should be of form: barcode quantity"
        )
    except ValueError:
        raise MalformedCommand(f"'{command}' is malformed, quantity must be an integer")
    return barcode, quantity
