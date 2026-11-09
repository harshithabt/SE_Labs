# Lab 5 - Static Code Analysis: Parking Lot System

---

This lab focuses on applying static code analysis techniques to identify, analyse, and resolve code quality, maintainability, and security issues in an existing Python-based Parking Lot System.

The original implementation was examined using static analysis tools, followed by code refactoring to address the identified issues while preserving the application's functionality.

## What was covered

- Static Code Analysis
- Code quality and maintainability assessment
- Security vulnerability detection
- Identification of code smells and potential errors
- Issue classification and prioritisation
- Code refactoring and security improvements
- Before-and-after analysis comparison
- Functional verification

## Tools Used

- **Pylint** – Code quality analysis and potential error detection.
- **Bandit** – Security vulnerability detection in Python code.
- **Flake8** – Code style and formatting checks.
- **Python** – Implementation and functional verification.

## Improvements Implemented

- Replaced unsafe dynamic evaluation with safer fee calculation.
- Removed unsafe shell command execution.
- Replaced MD5 hashing with SHA-256.
- Used the `secrets` module for secure PIN generation.
- Improved exception handling and input validation.
- Removed mutable default arguments and unnecessary global state.
- Improved naming conventions, documentation, and type annotations.
- Implemented safer JSON manifest export.

## Static Analysis Results

| Tool | Before Refactoring | After Refactoring |
|---|---:|---:|
| Pylint | 4.10/10 | 10.00/10 |
| Bandit | 5 findings | 0 findings |
| Flake8 | 10 violations | 0 violations |

The final implementation also passed Python compilation, focused behaviour assertions, and normal program execution.

## Deliverables

| Deliverable | Location |
|---|---|
| Refactored source code | `parking_lot_system.py` |
| Documented issues and fixes | `issues.md` |
| Reflection responses | `reflection.md` |
| Original implementation analysis | `reports/before/` |
| Refactored implementation analysis | `reports/after/` |

The before-and-after reports preserve the results obtained from analysing the original starter implementation and the final refactored implementation, respectively.

## Related Repository

[View the individual Lab 5 development and submission repository](https://github.com/harshithabt/L5_51_parking_lot_system)

## Author

**Harshitha B.T – PES1UG24AM118 (AIML-B Section)**

**Course:** Software Engineering Laboratory

---
