"""Property-based fuzz tests for the Self Storage input-processing functions."""

import math

import pytest
from hypothesis import given, strategies as st

from self_storage import duration_average, parse_rental, payable_rent


SAFE_UNIT = st.text(alphabet=st.characters(blacklist_characters=":\r\n"), min_size=1, max_size=25).filter(
    lambda value: bool(value.strip())
)


@given(SAFE_UNIT, st.floats(min_value=0, max_value=1_000_000, allow_nan=False, allow_infinity=False))
def test_parse_rental_valid_generated_inputs(unit, months):
    parsed_unit, parsed_months = parse_rental(f"{unit}:{months}")
    assert parsed_unit == unit.strip().title()
    assert math.isclose(parsed_months, months, rel_tol=1e-12, abs_tol=1e-12)


@given(st.one_of(st.text(max_size=80), st.none(), st.integers(), st.floats(allow_nan=True, allow_infinity=True)))
def test_parse_rental_arbitrary_input_is_safe(value):
    if isinstance(value, str) and value.count(":") == 1:
        unit, months_text = value.split(":")
        try:
            months = float(months_text.strip())
        except ValueError:
            months = None
        if unit.strip() and months is not None and math.isfinite(months) and months >= 0:
            result = parse_rental(value)
            assert isinstance(result, tuple) and len(result) == 2
            return
    with pytest.raises(ValueError):
        parse_rental(value)


@given(st.lists(st.integers(min_value=0, max_value=100_000), min_size=1, max_size=30))
def test_duration_average_generated_integer_lists(values):
    encoded = ",".join(str(value) for value in values)
    assert duration_average(encoded) == sum(values) // len(values)


@given(st.one_of(st.text(max_size=100), st.none(), st.integers(), st.floats(allow_nan=True, allow_infinity=True)))
def test_duration_average_arbitrary_input_is_safe(value):
    if isinstance(value, str):
        fields = value.split(",")
        try:
            parsed = [int(field.strip()) for field in fields]
        except ValueError:
            parsed = None
        if fields and all(field.strip() for field in fields) and parsed is not None and all(item >= 0 for item in parsed):
            assert duration_average(value) == sum(parsed) // len(parsed)
            return
    with pytest.raises(ValueError):
        duration_average(value)


@given(
    st.floats(min_value=0, max_value=1_000_000, allow_nan=False, allow_infinity=False),
    st.floats(min_value=0, max_value=1_000_000, allow_nan=False, allow_infinity=False),
)
def test_payable_rent_generated_amounts(rent, discount):
    expected = max(rent * 1.18 - discount, 0)
    assert math.isclose(payable_rent(f"{rent}|{discount}"), expected, rel_tol=1e-12, abs_tol=1e-9)


@given(st.one_of(st.text(max_size=100), st.none(), st.integers(), st.floats(allow_nan=True, allow_infinity=True)))
def test_payable_rent_arbitrary_input_is_safe(value):
    if isinstance(value, str) and value.count("|") == 1:
        rent_text, discount_text = value.split("|")
        try:
            rent = float(rent_text.strip())
            discount = float(discount_text.strip())
        except ValueError:
            rent = discount = None
        if rent is not None and discount is not None and math.isfinite(rent) and math.isfinite(discount) and rent >= 0 and discount >= 0:
            assert math.isclose(payable_rent(value), max(rent * 1.18 - discount, 0), rel_tol=1e-12, abs_tol=1e-9)
            return
    with pytest.raises(ValueError):
        payable_rent(value)
