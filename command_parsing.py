from typing import Optional

from cart import Cart, format_total

COMMAND_FINISH = "finish"
COMMAND_TOTAL = "total"


def parse_command(command: str, cart: Cart) -> Optional[str]:
    if command == COMMAND_TOTAL:
        return format_total(cart.total_in_cents())
    elif command == COMMAND_FINISH:
        cart.finish_sale()
    return None
