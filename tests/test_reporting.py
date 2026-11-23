import pytest

from src.reporting import (
    shipping_cost,
    loyalty_discount,
    final_amount,
    order_summary,
)


@pytest.mark.parametrize(
    "subtotal, express, expected",
    [
        (20, False, 10.0),
        (60, False, 5.0),
        (120, False, 0.0),
        (20, True, 15.0),
    ],
)
def test_shipping_cost(subtotal, express, expected):
    assert shipping_cost(subtotal, express) == expected


def test_shipping_negative_amount():
    with pytest.raises(ValueError):
        shipping_cost(-10)


@pytest.mark.parametrize(
    "points, expected",
    [
        (0, 0.0),
        (50, 5.0),
        (100, 10.0),
        (200, 15.0),
    ],
)
def test_loyalty_discount(points, expected):
    assert loyalty_discount(100, points) == expected


def test_loyalty_negative_amount():
    with pytest.raises(ValueError):
        loyalty_discount(-10, 0)


def test_loyalty_negative_points():
    with pytest.raises(ValueError):
        loyalty_discount(100, -1)


def test_final_amount():
    assert final_amount(100, points=100) == 90.0
    assert final_amount(0) == 10.0
    assert final_amount(10, express=True) == 25.0


@pytest.mark.parametrize(
    "subtotal, points, express, category",
    [
        (5, 0, False, "petite"),
        (40, 0, True, "moyenne"),
        (120, 0, False, "importante"),
    ],
)
def test_order_summary(subtotal, points, express, category):
    result = order_summary(subtotal, points, express)
    assert category in result
