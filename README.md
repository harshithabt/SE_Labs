# Software Engineering | UE24CS341A 

---

## Student Details 

| **Name: HARSHITHA.B.T** | **SRN: PES1UG24AM118** | **Section: AIML - “B”** |
|---|---|---|


## About This Repository

A collection of Software Engineering lab assignments completed as part of the **Software Engineering course** in the CSE – AIML curriculum at PES University.

It brings together the work completed across seven laboratory assignments, covering different stages and aspects of software development, including requirements engineering, agile project management, software architecture, AI-assisted development, static code analysis, software testing, code coverage, and fuzz testing.

Each lab is organized into its respective directory, containing the relevant source code, documentation, reports, screenshots, and other submission deliverables.

The repository provides a consolidated record of the concepts explored, techniques applied, and implementations developed throughout the course.

---

## Course Overview

The assignments explore practical software engineering concepts through the following areas:

- Requirements engineering and system requirements analysis.
- Agile methodologies, backlog management, and sprint planning.
- Component modelling and architectural design.
- AI-assisted development and Vibe Coding.
- Static code analysis and software quality assessment.
- Statement coverage and branch coverage testing.
- Property-based testing, fuzz testing, and input validation.

---

## Lab Submissions

| Lab | Topic | Description |
|---|---|---|
| **Lab 01** | Requirements Engineering and System Requirements | Analysing system requirements and preparing requirements documentation for the assigned application. |
| **Lab 02** | Agile Backlog Creation and Sprint Simulation | Creating and prioritizing an agile backlog, estimating user stories, and carrying out sprint planning activities. |
| **Lab 03** | Component Modelling and Architectural Pattern Selection | Modelling system components and documenting architectural design decisions and patterns. |
| **Lab 04** | Vibe Coding – Rhythm Tap | Understanding, fixing, and extending an existing Python rhythm game using Pygame and a Vibe Coding tool. |
| **Lab 05** | Static Code Analysis – Parking Lot System | Applying static analysis tools to identify code quality issues and evaluate improvements in a Python application. |
| **Lab 06** | Code and Branch Coverage Analysis – Self Storage | Designing and executing test cases to measure statement and branch coverage, achieving 100% coverage in both. |
| **Lab 07** | Fuzz Testing – Self Storage | Applying property-based testing using Hypothesis to identify input validation bugs and improve application robustness. |

---

## Repository Structure

The repository is organized by laboratory assignment. Each lab contains its corresponding source code, documentation, reports, screenshots, and supporting evidence.

```text
SE_Labs/
│
├── Lab01/
│   ├── PES1UG24AM118-Lab1 Report (BSection).pdf
│   └── README.md
│
├── Lab02/
│   ├── PES1UG24AM118-Lab2 Report (BSection).pdf
│   └── README.md
│
├── Lab03/
│   ├── PES1UG24AM118-Lab3 Report (BSection).pdf
│   ├── PES1UG24AM118_uml_diagram_lab03.png
│   └── README.md
│
├── Lab04/
│   ├── code/
│   │   ├── game/
│   │   │   ├── __init__.py
│   │   │   ├── beat.py
│   │   │   └── game_engine.py
│   │   ├── .gitignore.txt
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── videos/
│   │   ├── after.mp4
│   │   └── before.mp4
│   ├── PES1UG24AM118_Lab 04_Chat_History.pdf
│   └── README.md
│
├── Lab05/
│   ├── code/
│   │   └── parking_lot_system.py
│   ├── reports/
│   │   ├── before/
│   │   │   ├── bandit_report.txt
│   │   │   ├── flake8_report.txt
│   │   │   └── pylint_report.txt
│   │   └── after/
│   │       ├── bandit_report.txt
│   │       ├── flake8_report.txt
│   │       └── pylint_report.txt
│   ├── .gitignore
│   ├── issues.md
│   ├── reflection.md
│   └── README.md
│
├── Lab06/
│   ├── code/
│   │   ├── BranchCoverageTest_self_storage.py
│   │   ├── CodeCoverageTest_self_storage.py
│   │   ├── self_storage.py
│   │   └── test_self_storage.py
│   ├── screenshots/
│   │   ├── branch_coverage.png
│   │   └── code_coverage.png
│   ├── .gitignore
│   └── README.md
│
├── Lab07/
│   ├── code/
│   │   ├── self_storage.py
│   │   └── test_self_storage.py
│   ├── screenshots/
│   │   ├── 1_buggy_run.png
│   │   ├── 2A_hypothesis_failures.png
│   │   ├── 2B_failure_summary.png
│   │   ├── 3_fixed_run.png
│   │   └── 4_tests_passing.png
│   ├── .gitignore
│   ├── requirements.txt
│   ├── PES1UG24AM118-Lab07 Report (BSection).pdf
│   └── README.md
│
└── README.md
```

---

## Lab 01 – Requirements Engineering and System Requirements

The first lab focuses on understanding requirements engineering and translating system needs into structured requirements documentation.

**Key activities**

- Analysing the problem domain and identifying system requirements.
- Understanding functional and non-functional requirements.
- Documenting the requirements of the assigned system.

**Deliverables**

- Requirements analysis and documentation.
- Lab submission report.

See [Lab01](Lab01/) for the corresponding submission materials.

---

## Lab 02 – Agile Backlog Creation and Sprint Simulation

The second lab introduces agile software development practices through backlog creation, prioritization, estimation, and sprint planning.

**Key activities**

- Creating and organizing an agile product backlog.
- Identifying and documenting user stories.
- Prioritizing requirements.
- Estimating story points.
- Planning and simulating sprint activities.

**Deliverables**

- Agile backlog and user stories.
- Sprint planning and simulation documentation.
- Lab submission report.

See [Lab02](Lab02/) for the corresponding submission materials.

---

## Lab 03 – Component Modelling and Architectural Pattern Selection

The third lab focuses on understanding software architecture through component modelling and architectural pattern selection.

**Key activities**

- Identifying and modelling system components.
- Understanding component interactions and dependencies.
- Evaluating suitable architectural patterns.
- Documenting architectural design decisions.

**Deliverables**

- Component modelling diagrams.
- Architectural pattern documentation.
- Lab submission report.

See [Lab03](Lab03/) for the corresponding submission materials.

---

## Lab 04 – Vibe Coding: Rhythm Tap

The fourth lab focuses on using a Vibe Coding tool to understand, fix, and extend an existing Python game.

The implementation adds sound effects, hold notes, BPM-synchronized note spawning, and a game-over grade summary.

**Implemented features**

- Sound effects for PERFECT, GREAT, and OK hits.
- Hold notes requiring sustained key presses.
- BPM-synchronized note spawning.
- Game-over summary with hit counts, accuracy, and maximum combo.

**Version Control**

The project was developed by modifying the assigned starter repository:

[SETAPESU26/51_rhythm-tap](https://github.com/SETAPESU26/51_rhythm-tap)

The implementation was maintained in a personal GitHub repository, with Git commits tracking development changes and feature implementation.

**Deliverables**

- Updated source code.
- Before-and-after gameplay recordings (approximately 10-second MP4 videos).
- Chat history exported as a PDF.

See [Lab04/README.md](Lab04/README.md) for detailed instructions, project structure, and deliverable locations.

**Dedicated development repository:** [51_rhythm-tap](https://github.com/harshithabt/51_rhythm-tap)

---

## Lab 05 – Static Code Analysis: Parking Lot System

The fifth lab focuses on applying static code analysis techniques to evaluate the quality and maintainability of a Python-based parking lot system.

The assignment involves analysing the application, identifying potential code quality issues, examining analysis reports, and documenting improvements.

**Key activities**

- Performing static analysis on the Python application.
- Identifying code quality issues and potential problems.
- Examining reports generated by Bandit, Flake8, and Pylint.
- Comparing analysis results before and after improvements.
- Documenting observations and reflections on code quality.

**Deliverables**

- Parking lot application source code.
- Static analysis reports.
- Issue documentation.
- Reflection document.

See [Lab05/README.md](Lab05/README.md) for the detailed implementation and submission materials.

**Dedicated development repository:** [L5_51_parking_lot_system](https://github.com/harshithabt/L5_51_parking_lot_system)

---

## Lab 06 – Code and Branch Coverage Analysis: Self Storage

The sixth lab focuses on understanding and measuring statement coverage and branch coverage through systematic software testing.

A Self Storage application is used to develop test cases that exercise the application's statements and decision branches. The objective is to achieve at least 90% code and branch coverage.

**Key activities**

- Understanding statement coverage and branch coverage.
- Designing test cases for application functions.
- Executing tests using Pytest.
- Measuring coverage using the Python Coverage package.
- Identifying uncovered statements and branches and improving test coverage.

**Verified results**

| Metric | Result |
|---|---:|
| Statement Coverage | **100%** |
| Branch Coverage | **100%** |
| Code Coverage Test Cases | 29 passed |
| Branch Coverage Test Cases | 27 passed |

**Deliverables**

- Self Storage application source code.
- Code coverage test implementation.
- Branch coverage test implementation.
- Code coverage execution screenshot.
- Branch coverage execution screenshot.
- Lab documentation.

See [Lab06/README.md](Lab06/README.md) for the detailed implementation, test execution instructions, and results.

**Development repository:** [L6_L7_51_self_storage](https://github.com/harshithabt/L6_L7_51_self_storage)

---

## Lab 07 – Fuzz Testing: Self Storage

The seventh lab explores fuzz testing and property-based testing using the Hypothesis framework.

The assignment focuses on generating a wide range of inputs, including malformed and unexpected values, to identify input validation issues in a Self Storage application.

The application is subsequently improved with input validation, and the updated implementation is tested using property-based test cases.

**Key activities**

- Understanding fuzz testing and property-based testing.
- Using Hypothesis to generate test inputs.
- Identifying failures in the original application.
- Analysing edge cases and malformed inputs.
- Implementing input validation and error handling.
- Re-running property-based tests against the corrected application.

**Verified results**

| Metric | Result |
|---|---:|
| Hypothesis test cases | 6 passed
| Final test execution | Successful |

**Deliverables**

- Corrected Self Storage application.
- Hypothesis-based test implementation.
- Requirements and dependencies.
- Screenshots documenting initial failures and corrected execution.
- Fuzz testing experiment report.

See [Lab07/README.md](Lab07/README.md) for the detailed implementation, testing instructions, and experiment results.

**Development repository:** [L6_L7_51_self_storage](https://github.com/harshithabt/L6_L7_51_self_storage)

---

## Tools and Technologies

| Area | Tools / Technologies |
|---|---|
| Programming | Python |
| Version Control | Git and GitHub |
| Game Development | Pygame |
| Project Management | Jira |
| Software Testing | Pytest |
| Coverage Analysis | Coverage.py |
| Property-Based Testing | Hypothesis |
| Static Code Analysis | Bandit, Flake8, Pylint |
| Modelling | UML and architectural diagrams |
| Documentation | Markdown, PDF |

---

## Deliverables

Each lab directory contains the corresponding coursework and submission materials, organized according to the requirements of the individual assignment.

These may include:

- Source code and test implementations.
- Lab-specific README documentation.
- Reports and written reflections.
- Screenshots and execution evidence.
- Videos and other supporting files.

---

**Software Engineering Course | PES University | CSE – AIML, Section B**

---
