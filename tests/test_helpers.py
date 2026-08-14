from helpers import total, total_by_category

def test_total_empty_list():
    empty_expenses = []
    assert total(empty_expenses) == 0

def test_total_expenses():
    expenses = [
        {'title': 'coffee', 'category': 'food', 'amount': 15.0},
        {'title': 'flight', 'category': 'travel', 'amount': 10.0},
        {'title': 'amburger', 'category': 'food', 'amount': 25.0}
    ]
    assert total(expenses) == 50.0

def test_total_by_category():
    expenses = [
        {'title': 'coffee', 'category': 'food', 'amount': 15.0},
        {'title': 'flight', 'category': 'travel', 'amount': 10.0},
        {'title': 'amburger', 'category': 'food', 'amount': 25.0}
    ]
    assert total_by_category(expenses)['food'] == 40
    assert total_by_category(expenses)['travel'] == 10
