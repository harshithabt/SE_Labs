# Lab 06 – Code and Branch Coverage Analysis

---

## Overview

This laboratory exercise focuses on analysing statement coverage and branch coverage in a Python-based Self Storage application. The objective is to evaluate test effectiveness, identify uncovered execution paths and develop additional test cases to achieve comprehensive coverage.

The application consists of three primary functions:

- `rent_due()` – Calculates the rental amount based on unit size, rental duration, climate control and membership status.
- `access_allowed()` – Determines whether storage access is permitted based on the time, visitor status and ownership.
- `payment_status()` – Determines payment status using payment due dates, autopay settings and previous late payments.

## Objectives

- Understand the concepts of code coverage and branch coverage.
- Analyse application execution paths.
- Develop test cases using `pytest`.
- Identify uncovered statements and conditional branches.
- Improve test coverage through additional test cases.
- Verify coverage using the Python `coverage` package.

## Implementation

Two separate test suites were developed to evaluate the application:

**1. Code Coverage Testing**

Test cases were designed to exercise the application's statements and verify the behaviour of its functions.

**2. Branch Coverage Testing**

Additional test cases were developed to exercise conditional outcomes and decision paths within the application.

The `coverage` package was used to measure statement and branch coverage, while `pytest` was used to execute the test suites.

## Tools and Technologies

- Python
- pytest
- coverage

## Results

| Metric | Result |
|---|---:|
| Code Coverage | 100% |
| Branch Coverage | 100% |
| Code Coverage Tests | 29 passed |
| Branch Coverage Tests | 27 passed |

Both coverage targets exceeded the required minimum of 90%.

## Deliverables

- `self_storage.py` – Application under test.
- `test_self_storage.py` – Original starter test file.
- `CodeCoverageTest_self_storage.py` – Additional code coverage test cases.
- `BranchCoverageTest_self_storage.py` – Additional branch coverage test cases.
- `screenshots/code_coverage.png` – Code coverage execution results.
- `screenshots/branch_coverage.png` – Branch coverage execution results.

## Learning Outcomes

- Understanding statement and branch coverage.
- Designing test cases for different execution paths.
- Evaluating test effectiveness using coverage metrics.
- Improving test completeness through systematic testing.

## Related Repository

[ L6_L7_51_self_storage – Lab 6 and Lab 7 Implementation ](https://github.com/harshithabt/L6_L7_51_self_storage/tree/main/Lab06)

---
