# Lab 5 – Reflection

## 1. What did you learn about static code analysis?

Static code analysis examines source code without executing the program. In this lab, Pylint, Bandit, and Flake8 helped identify different categories of issues in the original Parking Lot System.

1. Pylint identified code-quality and maintainability problems, including missing documentation, inconsistent naming, mutable default arguments, broad exception handling, and unused variables. 
2. Bandit identified security-related issues such as dynamic expression evaluation using `eval()`, weak MD5 hashing, predictable random-number generation, shell command execution, and broad exception handling. 
3. Flake8 identified formatting and coding-standard violations, including overlong lines, unused imports, and other code issues.

I also learned that static analysis tools have different detection capabilities. Manual code review and behaviour testing are important because no single tool can identify every possible problem.

## 2. Which issues did you identify and fix?

The original Parking Lot System contained several security, reliability, and maintainability issues.

The major issues included dynamic expression evaluation using `eval()`, shell command execution using `os.system()`, MD5 hashing, predictable ticket PIN generation using `random.randint()`, a hard-coded barrier token, a mutable default list, bare exception handling, insufficient input validation, global mutable collection state, unused variables, inconsistent naming, missing type hints and documentation, and an unconditional `main()` call.

These issues were addressed through the refactoring process. Dynamic evaluation was replaced with validated numeric fee calculation, shell execution was removed, SHA-256 replaced MD5, and secure PIN generation was implemented using Python's `secrets` module. Input validation, explicit exception handling, structured JSON export, type hints, docstrings, and a guarded program entry point were also introduced.

The original reports are retained in reports/before/, while the reports generated after refactoring are retained in reports/after/. This allows the analysis results to be compared directly.

The original static-analysis reports also identified code-quality and security findings, which were addressed during the refactoring process.

## 3. How did static analysis improve the program?

The analysis and refactoring process improved the program's security, readability, reliability, and maintainability.

The final implementation uses a `ParkingLotState` dataclass to manage collection state, type annotations to clarify function contracts, consistent snake_case naming, and documentation for functions and data structures. It also uses validated fee calculations, SHA-256 hashing, cryptographically secure PIN generation, and safe JSON file handling.

The final verification produced the following results:

- Pylint: **10.00/10**.
- Bandit: **No issues identified**.
- Flake8: **No violations reported**.
- Python compilation: Passed.
- Focused behaviour assertions: Passed.
- Normal program execution: Passed.

These results demonstrate that the refactored implementation satisfies the static-analysis checks performed and passed the additional functional checks carried out.

## 4. What are the limitations of static code analysis?

Static analysis cannot prove that a program is completely correct or identify every possible runtime problem. A tool may fail to detect an issue if the relevant pattern is not recognised or if the issue depends on runtime input and behaviour.

The original program also demonstrated why manual review is necessary: security and design problems need to be understood in the context of how the application works, rather than relying exclusively on tool output.

Therefore, the final assessment combined static-analysis reports with manual source-code review, Python compilation, focused behaviour assertions, and normal program execution. This provided a more complete evaluation of the Parking Lot System than static analysis alone.
