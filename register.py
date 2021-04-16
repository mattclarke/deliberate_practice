import cmd
from typing import Optional

from catalogue import Catalogue
from cart import Cart
from command_parsing import (
    COMMANDS,
    execute_command_scan,
    COMMAND_SCAN,
    execute_command_total,
    COMMAND_TOTAL,
    execute_command_finish,
    COMMAND_FINISH,
)
from typing import List


def split_command(cmd_arg: str) -> List[str]:
    return cmd_arg.strip().split(" ")


class CashRegister(cmd.Cmd):
    intro = "Welcome to the cash register!"
    prompt = "> "

    def __init__(self, catalogue: Catalogue):
        super().__init__()
        self.system = Cart(catalogue)

    def do_help(self, arg: str) -> Optional[bool]:
        print(f"Commands are: {', '.join(COMMANDS)}")
        return None

    def do_quit(self, arg: str) -> Optional[bool]:
        return True

    def do_scan(self, arg: str) -> Optional[bool]:
        execute_command_scan(self.system, split_command(arg), f"{COMMAND_SCAN} {arg}")
        return None

    def do_finish(self, arg: str) -> Optional[bool]:
        execute_command_finish(
            self.system, split_command(arg), f"{COMMAND_FINISH} {arg}"
        )
        return None

    def do_total(self, arg: str) -> Optional[bool]:
        print(
            execute_command_total(
                self.system, split_command(arg), f"{COMMAND_TOTAL} {arg}"
            )
        )
        return None

    def precmd(self, line: str) -> str:
        return line.strip()


if __name__ == "__main__":
    catalogue = Catalogue()
    catalogue.add_new_product("12345", 345)
    catalogue.add_new_product("23456", 273, is_taxable=True)

    CashRegister(catalogue).cmdloop()
