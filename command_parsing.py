from typing import Optional, List, Tuple

from cart import Cart, format_total
from exceptions import UnrecognisedCommand, MalformedCommand

COMMAND_FINISH = "finish"
COMMAND_TOTAL = "total"
COMMAND_SCAN = "scan"
COMMANDS = {COMMAND_SCAN, COMMAND_FINISH, COMMAND_TOTAL}


def parse_command(command_input: str, cart: Cart) -> Optional[str]:
    split_command = command_input.strip().split(" ")
    command = split_command[0]

    if command == COMMAND_TOTAL:
        return execute_command_total(cart, split_command, command)
    elif command == COMMAND_FINISH:
        execute_command_finish(cart, split_command, command)
    elif command == COMMAND_SCAN:
        execute_comand_scan(cart, split_command, command)
    else:
        raise UnrecognisedCommand(f"'{command}' is not a recognised command")
    return None


def execute_comand_scan(cart: Cart, split_command: List[str], command: str):
    if len(split_command) > 3:
        raise MalformedCommand(
            f"'{command}' is malformed, should be of form: barcode quantity"
        )
    try:
        barcode, quantity = _get_barcode_and_quantity(command, split_command)
        cart.add_item_by_barcode(barcode, quantity)
    except IndexError:
        raise MalformedCommand(
            f"'{command}' is malformed, should be of form: barcode quantity"
        )


def execute_command_finish(cart: Cart, split_command: List[str], command: str):
    if len(split_command) != 1:
        raise MalformedCommand(
            f"'{command}' is malformed as it does not take parameters"
        )
    cart.finish_sale()


def execute_command_total(cart: Cart, split_command: List[str], command: str):
    if len(split_command) != 1:
        raise MalformedCommand(
            f"'{command}' is malformed as it does not take parameters"
        )
    return format_total(cart.total_in_cents())


def _get_barcode_and_quantity(
    command: str, split_command: List[str]
) -> Tuple[str, int]:
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
