# Lab 5 – Static Analysis Findings

## 1. Overview

This document records the issues identified in the original Parking Lot System implementation and the improvements made during Lab 5.

The original source code was obtained from the assigned GitHub repository:

**Original repository:** https://github.com/SETAPESU26/L5_51_parking_lot_system

The original implementation was analysed using Pylint, Bandit, and Flake8. The tool findings were supplemented with manual code review to identify additional security, reliability, and maintainability issues.

The original and final analysis reports are preserved in `reports/before/` and `reports/after/`, respectively.

## 2. Identified Issues and Fixes

| No. | Issue | Category / Severity | Original Source / Evidence | Fix Implemented |
|---|---|---|---|---|
| 1 | Dynamic expression evaluation using `eval()` | Security / High | Original `calculateParkingFee()` used `eval(surge_expr)`. Bandit B307. | Replaced expression evaluation with a numeric surge multiplier, finite and non-negative validation, and direct arithmetic. |
| 2 | Shell command execution using `os.system()` | Security / High | Original `exportParkingManifest()` constructed and executed a shell command. Bandit B605. | Removed shell execution and exported the manifest using `pathlib` and JSON. |
| 3 | Weak MD5 vehicle hashing | Security / High | Original `generateVehicleHash()` used MD5. Bandit B324. | Replaced MD5 with SHA-256. |
| 4 | Predictable ticket PIN generation | Security / Medium | Original `generateTicketPin()` used `random.randint()`. Bandit B311. | Replaced the pseudo-random generator with `secrets.randbelow()`. |
| 5 | Hard-coded barrier secret | Security / Medium | Original implementation contained a hard-coded barrier token. | Removed the exposed token and retained a non-secret configuration-status demonstration. |
| 6 | Mutable default argument | Reliability / Medium | Original `parkVehicle()` used `entry_logs=[]`. Pylint W0102. | Changed the default to `None` and created a fresh list when needed. |
| 7 | Bare exception handling | Reliability / Medium | Original `releaseSlot()` used a bare `except`. Pylint W0702 and Bandit B110. | Replaced blanket exception handling with explicit missing-slot handling and Boolean return values. |
| 8 | Missing input validation | Reliability / Medium | Original parking operation did not adequately validate vehicle plate numbers and booking duration. | Added validation for non-empty plate numbers and positive booking duration. |
| 9 | Unsafe fee calculation | Security / Medium | Original fee calculation accepted a dynamically evaluated expression. | Added slot validation and numeric, finite, non-negative surge-multiplier validation. |
| 10 | Global mutable collection state | Maintainability / Medium | Original implementation updated `total_collections` through a global variable. Pylint W0603. | Introduced a `ParkingLotState` dataclass and `get_total_collections()` to manage collection state explicitly. |
| 11 | Unused variables | Code Quality / Low | Original implementation contained unused variables such as `overtime_fee` and `base_rate`. Pylint and Flake8 findings. | Removed unused variables. |
| 12 | Comparison with `None` using `==` | Code Quality / Low | Original availability check used `== None`. Pylint C0121 and Flake8 E711. | Replaced the comparison with explicit `None` handling. |
| 13 | Manual file handling | Reliability / Medium | Original manifest export used explicit `open()` and `close()` calls. Pylint W1514 and R1732. | Used a context manager with UTF-8 encoding. |
| 14 | Manifest stored as a string representation | Maintainability / Low | Original manifest was stored as a string representation in a `.txt` file. | Exported structured JSON to a `.json` file. |
| 15 | Inconsistent function naming | Maintainability / Low | Original functions used camelCase names such as `parkVehicle()` and `releaseSlot()`. Pylint C0103. | Renamed functions using consistent snake_case identifiers. |
| 16 | Missing type hints and unclear function contracts | Maintainability / Low | Original functions lacked parameter and return annotations. | Added type hints, `TypedDict`, and explicit return types. |
| 17 | Missing documentation | Maintainability / Low | Original functions and data structures lacked documentation. Pylint C0114 and C0116. | Added module, function, and data-structure docstrings. |
| 18 | Unconditional `main()` call on import | Maintainability / Low | Original program called `main()` directly at module level. | Added the `if __name__ == "__main__":` entry-point guard. |
| 19 | Unclear slot-release return contract | Reliability / Low | Original `releaseSlot()` did not provide a clear success/failure result. | Updated `release_slot()` to return `True` for a known slot and `False` otherwise. |

## 3. Original Static Analysis Results

The reports in `reports/before/` were generated against the original GitHub starter implementation.

### Pylint

- Original score: **4.10/10**.
- Findings included missing documentation, inconsistent naming, mutable default arguments, broad exception handling, unused variables, dynamic evaluation, and other code-quality issues.

### Bandit

Bandit identified **5 findings**:

- B110 – Try/except/pass detected.
- B307 – Use of a potentially insecure function (`eval()`).
- B324 – Weak MD5 hashing.
- B311 – Standard pseudo-random generator used for PIN generation.
- B605 – Starting a process with a shell.

### Flake8

Flake8 identified **10 violations**, including:

- Unused imports.
- Overlong lines.
- Bare exception handling.
- Unused local variables.
- Incorrect comparison with `None`.
- Missing newline at the end of the file.

## 4. Final Static Analysis Results

After refactoring, the analysis tools were executed again against the final `parking_lot_system.py`.

| Tool | Original Implementation | Final Implementation |
|---|---:|---:|
| Pylint | 4.10/10 | **10.00/10** |
| Bandit | 5 findings | **0 findings** |
| Flake8 | 10 violations | **0 violations** |

## 5. Additional Verification

The final implementation was also checked through:

- Python compilation using `py_compile`.
- Focused behaviour assertions for parking and slot release.
- Collection tracking.
- Parking fee calculation and surge multiplier validation.
- SHA-256 hash generation.
- Secure ticket PIN generation.
- Normal program execution.

All recorded checks passed.

## 6. Conclusion

The static analysis process helped identify security, reliability, code-quality, and maintainability issues in the original Parking Lot System.

The final implementation addresses the documented issues and achieves a Pylint score of 10.00/10, with no reported Bandit findings or Flake8 violations.