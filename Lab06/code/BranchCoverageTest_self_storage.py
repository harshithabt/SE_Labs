"""Tests explicitly exercising True and False outcomes of decision branches."""

import pytest

from self_storage import access_allowed, payment_status, rent_due


@pytest.mark.parametrize("size", ["small", "medium", "large"])
def test_valid_unit_size_branch(size):
    assert rent_due(size, 0, False, False) == 0


def test_invalid_unit_size_branch():
    with pytest.raises(ValueError, match="unknown unit size"):
        rent_due("unknown", 1, False, False)


def test_negative_months_branch():
    with pytest.raises(ValueError, match="invalid months"):
        rent_due("medium", -2, False, False)


@pytest.mark.parametrize(
    "size,months,member,expected",
    [
        ("small", 2, True, 0),       # member and not large: covered += 1
        ("large", 2, True, 0),       # member but large: no extra covered month
        ("small", 2, False, 80),     # non-member
        ("small", 1, False, 0),      # extra <= 0
    ],
)
def test_member_and_extra_month_branches(size, months, member, expected):
    assert rent_due(size, months, False, member) == expected


@pytest.mark.parametrize(
    "climate,extra_months,expected",
    [
        (True, 2, 240),
        (False, 2, 160),
        (True, 7, 735),
        (False, 7, 490),
    ],
)
def test_climate_and_long_term_rate_branches(climate, extra_months, expected):
    assert rent_due("small", 1 + extra_months, climate, False) == expected


@pytest.mark.parametrize(
    "hour,visitors,owner,expected",
    [
        (0, 4, True, True),
        (12, 5, True, False),
        (5, 1, False, False),
        (23, 1, False, False),
        (6, 2, False, True),
        (22, 3, False, False),
        (12, 1, False, True),
    ],
)
def test_access_control_decisions(hour, visitors, owner, expected):
    assert access_allowed(hour, visitors, owner) is expected


@pytest.mark.parametrize(
    "days,autopay,late,expected",
    [
        (0, True, False, "current"),
        (0, False, False, "grace"),
        (5, False, False, "current"),
        (-11, False, False, "lien"),
        (15, False, True, "current"),
        (0, False, True, "grace"),
        (-6, False, True, "lien"),
    ],
)
def test_payment_cutoff_and_status_branches(days, autopay, late, expected):
    assert payment_status(days, autopay, late) == expected
