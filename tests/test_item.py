"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def test():
    return Item("Смартфон", 100, 1)


def test_item_init(test):
    assert test.name == "Смартфон"
    assert test.price == 100
    assert test.quantity == 1


def test_calculate_total_price(test):
    assert test.calculate_total_price() == 100


def test_apply_discount(test):
    Item.pay_rate = 0.8
    test.apply_discount()
    assert test.price == 80
