from typing import List, Tuple

from cart import Cart, format_total
from exceptions import MalformedCommand

COMMAND_FINISH = "finish"
COMMAND_TOTAL = "total"
COMMAND_SCAN = "scan"
COMMANDS = {COMMAND_SCAN, COMMAND_FINISH, COMMAND_TOTAL}


def execute_command_scan(cart: Cart, split_command: List[str], command: str):
    if len(split_command) > 2:
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


def execute_command_finish(cart: Cart, args: List[str], command: str):
    if args:
        raise MalformedCommand(
            f"'{command}' is malformed as it does not take parameters"
        )
    cart.finish_sale()


def execute_command_total(cart: Cart, args: List[str], command: str):
    if args:
        raise MalformedCommand(
            f"'{command}' is malformed as it does not take parameters"
        )
    return format_total(cart.gross_total())


def _get_barcode_and_quantity(
    command: str, split_command: List[str]
) -> Tuple[str, int]:
    try:
        barcode = split_command[0]
        quantity = int(split_command[1])
    except IndexError:
        raise MalformedCommand(
            f"'{command}' is malformed, should be of form: barcode quantity"
        )
    except ValueError:
        raise MalformedCommand(f"'{command}' is malformed, quantity must be an integer")
    return barcode, quantity
