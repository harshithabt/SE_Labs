"""Tests targeting statement (line) coverage for self_storage.py."""

import pytest

from self_storage import access_allowed, payment_status, rent_due


@pytest.mark.parametrize(
    "unit_size,months,is_climate,is_member,expected",
    [
        ("small", 1, False, False, 0),
        ("medium", 2, True, False, 0),
        ("large", 3, False, True, 0),
        ("small", 3, False, False, 160),
        ("small", 3, True, False, 240),
        ("small", 9, False, False, 560),
        ("small", 9, True, False, 840),
        ("small", 3, False, True, 80),
        ("large", 5, False, True, 160),
    ],
)
def test_rent_due_scenarios(unit_size, months, is_climate, is_member, expected):
    assert rent_due(unit_size, months, is_climate, is_member) == expected


@pytest.mark.parametrize("unit_size", ["tiny", "extra-large", ""])
def test_unknown_unit_size_raises(unit_size):
    with pytest.raises(ValueError, match="unknown unit size"):
        rent_due(unit_size, 2, False, False)


def test_negative_months_raise():
    with pytest.raises(ValueError, match="invalid months"):
        rent_due("small", -1, False, False)


@pytest.mark.parametrize(
    "hour,visitors,is_owner,expected",
    [
        (2, 4, True, True),
        (12, 5, True, False),
        (5, 1, False, False),
        (23, 1, False, False),
        (6, 2, False, True),
        (22, 3, False, False),
        (12, 2, False, True),
    ],
)
def test_access_allowed_scenarios(hour, visitors, is_owner, expected):
    assert access_allowed(hour, visitors, is_owner) is expected


@pytest.mark.parametrize(
    "days,is_autopay,has_prior_late,expected",
    [
        (0, True, False, "current"),
        (-1, True, False, "grace"),
        (-16, True, False, "lien"),
        (5, False, False, "current"),
        (0, False, False, "grace"),
        (-11, False, False, "lien"),
        (15, False, True, "current"),
        (0, False, True, "grace"),
        (-6, False, True, "lien"),
    ],
)
def test_payment_status_scenarios(days, is_autopay, has_prior_late, expected):
    assert payment_status(days, is_autopay, has_prior_late) == expected
