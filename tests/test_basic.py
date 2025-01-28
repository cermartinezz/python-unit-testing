def calculate_total(products, discount=0):
    total = 0
    for product in products:
        total += product['price']
    total = total - (total * discount/100)
    return total

def test_calculate_total_multiple_products():
    products = [
        {'name': 'Product 1', 'price': 100},
        {'name': 'Product 2', 'price': 200},
    ]
    assert calculate_total(products) == 300

def test_calculate_total_single_products():
    products = [
        {'name': 'Product 1', 'price': 100},
    ]
    assert calculate_total(products) == 100

def test_calculate_total_empty_products():
    products = []
    assert calculate_total(products) == 0

def test_calculate_total_with_10_percent_discount():
    products = [
        {'name': 'Product 1', 'price': 100},
        {'name': 'Product 2', 'price': 200},
    ]
    assert calculate_total(products, 10) == 270

if __name__ == '__main__':
    test_calculate_total_single_products()
    test_calculate_total_multiple_products()
    test_calculate_total_empty_products()
    test_calculate_total_with_10_percent_discount()
    print('All tests passed')

