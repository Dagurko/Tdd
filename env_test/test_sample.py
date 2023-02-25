import pytest
import sample


def test_single_item_no_taxes_or_shipping():
    item_list = {'item_1': 1}
    location = 'Iceland'
    result = sample.calculate_order(item_list, location)
    assert result[1] == 10

    