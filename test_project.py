from project import add_expense, delete_expense, total_spent, total_by_cat
from datetime import date
import pytest


def test_add_expense():
    result = add_expense([], 100, "food", date(2026, 10, 21), "lunch")
    assert len(result) == 1
    assert result[0]["amount"] == 100


def test_add_expense_invalid():
    with pytest.raises(ValueError):
        add_expense([], -5, "food", date(2026, 10, 21))


def test_delete_expense():
    expenses = [{"amount": 10}, {"amount": 20}]
    result = delete_expense(expenses, 0)
    assert len(result) == 1
    assert result[0]["amount"] == 20


def test_total_spent():
    expenses = [{"amount": 250.0}, {"amount": 80.0}]
    assert total_spent(expenses) == 330.0


def test_total_by_cat():
    expenses = [
        {"category": "food", "amount": 250.0},
        {"category": "food", "amount": 100.0},
        {"category": "travel", "amount": 80.0},
    ]
    assert total_by_cat(expenses) == {"food": 350.0, "travel": 80.0}
