TAX_RATES = {'Iceland': 0.24, 
             'France': 0.2, 
             'Denmark': 0.15 }

SHIPPING_FEES = {'Iceland': {1: 14.75, 5: 24, 10: 39.25}, 
                 'France': {1: 17.5 , 5: 28.7 , 10: 44.55}, 
                 'Denmark': {1: 17.5 , 5: 28.7 , 10: 44.55}}

ITEM = {'item_1': {'price': 10, 'weight': 1},
        'item_2': {'price': 50, 'weight': 5}, 
        'item_3': {'price': 35, 'weight': 1}, 
        'item_4': {'price': 90, 'weight': 10}, 
        'item_5': {'price':100, 'weight': 5}}

def calculate_order(item_list, location):
    subtotal = 0
    shipping_fees = 0
    for item, quantity in item_list.items():
        subtotal += (ITEM[item]['price'] * quantity) 
        shipping_fees += (SHIPPING_FEES[location][ITEM[item]['weight']]*quantity)
    tax = subtotal * TAX_RATES[location]
    total = subtotal + tax + shipping_fees
    return (total, subtotal, tax, shipping_fees)



def test_single_item_no_taxes_or_shipping():
    item_list = {'item_1': 1}
    location = 'Iceland'
    result = calculate_order(item_list, location)
    assert result[1] == 10

