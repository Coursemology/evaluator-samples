---
# Evaluator Samples

This repository contains sample test packages for [Coursemology](https://github.com/Coursemology/coursemology2)'s code [evaluator](https://github.com/Coursemology/evaluator-slave), which is used to evaluate students' submissions for coding exercises on Coursemology. The evaluator is designed to evaluate submissions for programming languages in general by riding on the unit test frameworks available for each programming language.

The samples in this repository are created to illustrate how tests to check if coding exercise submissions satisfy the objectives of the exercise should be written. The tests can go beyond checking if the submitted code outputs the right answer. For example, tests can be written to check if the submitted code is an iterative rather than recursive solution.

---
# Expected Test Package Structure

The evaluator expects a ZIP archive with a Makefile and a `submission` folder. The `submission` folder contains the initial code templates provided to students for the programming exercise. The students are expected to modify the code templates to complete the exercise. The evaluator populates the database with metadata for the tests by unzipping the archive and parsing the unit test report file from running `make test` on the resulting folder.

For coding exercises where the template given has syntax errors or infinite loops, a `solution` folder with working code for the exercise must be provided.

The exact location of the files containing tests for submissions to the coding exercise is defined by the Makefile.

---
# Makefile

The Makefile must contain the following make targets.

1. `prepare`
2. `compile`
3. `test`

These 3 targets will be run by the evaluator in the order shown above.

A successful evaluation must produce a file named `report.xml`.
A sample report file is available in the `sample_reports` folder.

---
# Python Test samples

The current test samples are specific to the [evaluator images](https://github.com/Coursemology/evaluator-images/tree/master/python/python3.5) deployed for CS1010S, which uses a [modified fork of python's unit test runner](https://github.com/Coursemology/unittest-xml-reporting/tree/extra-attributes).

### Code structure for programming exercises with runnable template code
```
sample_tests.zip
    |
    +-- Makefile
    +-- submission
      |
      +-- template.py
    +-- tests
      |
      +-- autograde.py
      +-- append.py
      +-- prepend.py
```

### Code structure for programming exercises with non runnable template code
```
sample_tests.zip
    |
    +-- Makefile
    +-- submission
      |
      +-- template.py
    +-- solution
      |
      +-- template.py
    +-- tests
      |
      +-- autograde.py
      +-- append.py
      +-- prepend.py
```

## Description of test files
The tests to be run on the students' submissions are in `autograde.py`. `prepend.py` consists of code to be prepended to the submissions before the tests are run, while `append.py` consists of code to be appended to the submissions before the tests are run.

The tests for a student's programming exercise are run by sending the package with the templates in the `submission` folder replaced by the student's submissions to the code evaluator. The evaluator generates a xml test report file by running `make test` on the package. The test report file is then retrieved by Coursemology to render the test results for the student.

### autograde.py
Each test to be executed on the students' code submissions must be written as methods of a class extending `unittest.TestCase` as required by the unit test framework.

The class must have the `setUp` instance method defined in the following manner:
```
def setUp(self):
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }
```
Public test cases are instance methods with names of the format: `test_public_*`

Private test cases are instance methods with names of the format: `test_private_*`

Evalution test cases, which are used to assign a preliminary grade to the programming exercise, are instance methods with names of the format: `test_evaluation_*`

Timeouts for each test case can be defined using the timeout decorator: @timeout_decorator.timeout(time-in-seconds)
