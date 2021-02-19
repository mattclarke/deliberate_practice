from cart import Cart
from catalogue import Catalogue
from command_parsing import parse_command, COMMAND_TOTAL, COMMAND_FINISH
from unittest import mock


def test_total_command_returns_string_to_display():
    cart = Cart(Catalogue())

    output = parse_command(COMMAND_TOTAL, cart)

    assert "$" in output


def test_finish_returns_none():
    mock_cart = mock.create_autospec(Cart)

    parse_command(COMMAND_FINISH, mock_cart)

    mock_cart.finish_sale.assert_called()
