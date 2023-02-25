TAX_RATES = {'Iceland': 0.24, 
             'France': 0.2, 
             'Denmark': 0.15 }

SHIPPING_FEES = {'Iceland': {1: 14.75, 2: 16.35, 4: 21.35, 5: 24, 6: 27.05, 7: 30.10, 8: 33.15, 9: 36.2, 10: 39.25}, 
                 'France': {1: 17.5, 2: 20.05, 3: 22.9, 4: 25.8, 5: 28.7, 6: 31.9, 7: 35.05, 8: 38.2, 9: 41.35, 10: 44.55}, 
                 'Denmark': {1: 17.5, 2: 20.05, 3: 22.90, 4: 25.8, 5: 28.7, 6: 31.9, 7: 25.05, 8: 38.2, 9: 41.35, 10: 44.55}}

ITEM = {'item_1': {'price': 10, 'weight': 2},
        'item_2': {'price': 50, 'weight': 3}, 
        'item_3': {'price': 35, 'weight': 5}, 
        'item_4': {'price': 90, 'weight': 1}, 
        'item_5': {'price':100, 'weight': 2}}

def calculate_order(item_list, location):
    subtotal = 0
    shipping_fees = 0
    weight = 0
    for item, quantity in item_list.items():
        subtotal += (ITEM[item]['price'] * quantity) 
        weight += ITEM[item]['weight'] * quantity
    shipping_fees = SHIPPING_FEES[location][weight]
    tax = subtotal * TAX_RATES[location]
    total = subtotal + tax + shipping_fees
    return (total, subtotal, tax, shipping_fees)





