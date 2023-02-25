import pytest
import sample
# ITEM = {'item_1': {'price': 10, 'weight': 1},
#         'item_2': {'price': 50, 'weight': 5}, 
#         'item_3': {'price': 35, 'weight': 1}, 
#         'item_4': {'price': 90, 'weight': 10}, 
#         'item_5': {'price':100, 'weight': 5}}

def test_single_item_no_taxes_or_shipping():
    item_list = {'item_1': 1}
    location = 'Iceland'
    result = sample.calculate_order(item_list, location)
    assert result[1] == 10

def test_multiple_items_no_taxes_or_shipping():
    item_list = {'item_1': 1, 'item_2': 1}
    location = 'Denmark'
    result = sample.calculate_order(item_list, location)
    assert result[1] == 60


    