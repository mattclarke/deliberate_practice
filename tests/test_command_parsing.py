from cart import Cart
from catalogue import Catalogue
from command_parsing import (
    execute_comand_scan,
    parse_command,
    COMMAND_TOTAL,
    COMMAND_FINISH,
    COMMAND_SCAN,
)
from exceptions import UnrecognisedCommand, MalformedCommand
from unittest import mock
import pytest


def test_total_command_requests_total():
    mock_cart = mock.create_autospec(Cart)
    mock_cart.gross_total.return_value = 100

    parse_command(COMMAND_TOTAL, mock_cart)

    mock_cart.gross_total.assert_called_once()


def test_finish_command_requests_finish():
    mock_cart = mock.create_autospec(Cart)

    parse_command(COMMAND_FINISH, mock_cart)

    mock_cart.finish_sale.assert_called_once()


def test_scan_command_is_processed():
    mock_cart = mock.create_autospec(Cart)

    barcode = "123"
    quantity = "2"
    command_input = [barcode, quantity]

    execute_comand_scan(mock_cart, command_input, COMMAND_SCAN)

    mock_cart.add_item_by_barcode.assert_called_once()


def test_exception_raised_on_unrecognised_command():
    cart = Cart(Catalogue())

    unknown_command = "UNKNOWN"

    with pytest.raises(UnrecognisedCommand):
        parse_command(unknown_command, cart)


def test_exception_raised_on_empty_command():
    cart = Cart(Catalogue())

    with pytest.raises(UnrecognisedCommand):
        parse_command("", cart)


def test_exception_raised_on_scan_with_no_barcode_etc():
    cart = Cart(Catalogue())

    incomplete_command = []

    with pytest.raises(MalformedCommand):
        execute_comand_scan(cart, incomplete_command, COMMAND_SCAN)


def test_exception_raised_on_scan_with_non_numeric_quantity():
    cart = Cart(Catalogue())

    scan_command = ["123", "abc"]

    with pytest.raises(MalformedCommand):
        execute_comand_scan(cart, scan_command, COMMAND_SCAN)


def test_exception_raised_on_scan_with_non_integer_quantity():
    cart = Cart(Catalogue())

    scan_args = ["123", "1.12"]

    with pytest.raises(MalformedCommand):
        execute_comand_scan(cart, scan_args, COMMAND_SCAN)


@pytest.mark.parametrize(
    "command, parameters",
    [
        (COMMAND_SCAN, "12345 1 ::extra::"),
        (
            COMMAND_FINISH,
            "::extra::",
        ),
        (COMMAND_TOTAL, "::extra::"),
    ],
)
def test_exception_raised_on_commands_with_too_many_parameters(command, parameters):
    cart = Cart(Catalogue())

    incomplete_command = f"{command} {parameters}"

    with pytest.raises(MalformedCommand):
        parse_command(incomplete_command, cart)
