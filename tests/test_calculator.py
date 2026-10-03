"""Tests for src.calculator module."""

import pytest

from src.calculator import add


class TestAddPositiveValues:
    """Tests with positive operands."""

    def test_two_positive_integers(self):
        assert add(2, 3) == 5

    def test_large_positive_integers(self):
        assert add(1000, 9000) == 10000

    def test_positive_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_positive_int_and_float(self):
        assert add(3, 0.14) == pytest.approx(3.14)


class TestAddNegativeValues:
    """Tests with negative operands."""

    def test_two_negative_integers(self):
        assert add(-4, -6) == -10

    def test_negative_and_positive_integer(self):
        assert add(-10, 3) == -7

    def test_positive_and_negative_integer(self):
        assert add(10, -3) == 7

    def test_negative_floats(self):
        assert add(-1.5, -2.5) == pytest.approx(-4.0)

    def test_negative_result_from_mixed_floats(self):
        assert add(-5.0, 2.0) == pytest.approx(-3.0)


class TestAddZeroValues:
    """Tests involving zero."""

    def test_zero_plus_zero(self):
        assert add(0, 0) == 0

    def test_zero_plus_positive(self):
        assert add(0, 7) == 7

    def test_positive_plus_zero(self):
        assert add(7, 0) == 7

    def test_zero_plus_negative(self):
        assert add(0, -5) == -5

    def test_negative_plus_zero(self):
        assert add(-5, 0) == -5

    def test_zero_float_operands(self):
        assert add(0.0, 0.0) == pytest.approx(0.0)

    def test_opposites_sum_to_zero(self):
        assert add(42, -42) == 0
