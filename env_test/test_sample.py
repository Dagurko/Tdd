import pytest
import sample


def test_single_item_no_taxes_or_shipping():
    item_list = {'item_3': 1}
    location = 'Iceland'
    result = sample.calculate_order(item_list, location)
    assert result[1] == 35

def test_multiple_items_no_taxes_or_shipping():
    item_list = {'item_1': 1, 'item_2': 1}
    location = 'Denmark'
    result = sample.calculate_order(item_list, location)
    assert result[1] == 60

def test_calculate_taxes_by_location():
    item_list = {'item_1': 1}
    location = 'Iceland'
    result = sample.calculate_order(item_list, location)
    assert result[2] == 2.4

def test_calculate_shipping_by_location_and_weight():
    item_list = {'item_1': 1, 'item_2': 1}
    location = 'France'
    result = sample.calculate_order(item_list, location)
    assert result[3] == 28.7


def test_total_cost_with_taxes_and_shipping():
    item_list = {'item_1': 2, 'item_4': 3, 'item_5': 1}
    location = 'France'
    result = sample.calculate_order(item_list, location)
    assert result[0] == 509.35


   