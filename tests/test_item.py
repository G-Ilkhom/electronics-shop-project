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

def test_name_setter(test):
    test.name = 'Телефон'
    assert test.name == 'Телефон'
    test.name = 'СуперСмартфон'
    assert test.name == 'Телефон'


def test_instantiate_from_csv(test):
    test.instantiate_from_csv()
    assert test.all[0].name == 'Смартфон'

def test_string_to_number(test):
    assert type(test.string_to_number('3')) == int