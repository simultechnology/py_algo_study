# Algorithm Study Project Guide

This guide explains how to use the Python algorithm study project with Poetry.

## 1. Environment Setup

### Installing Poetry

If you haven't installed Poetry yet, install it with the following command:

```bash
# macOS / Linux / Windows
curl -sSL https://install.python-poetry.org | python3 -

# Or using pip
pip install poetry
```

### Project Setup

Navigate to the project directory and install dependencies:

```bash
cd /Users/t_ishikawa/workspace/python_work/py_algo_study
poetry install
```

This will install all dependencies listed in `pyproject.toml`.

## 2. Using the Virtual Environment

Poetry automatically creates a virtual environment. Activate it with:

```bash
poetry shell
```

Alternatively, you can prefix commands with `poetry run`:

```bash
poetry run python -m py_algo_study.algorithms.sorting.quick_sort
```

## 3. Running Algorithms

### Run a Single Algorithm

```bash
# Run the quicksort example
poetry run python -m py_algo_study.algorithms.sorting.quick_sort
```

### Run Benchmarks

```bash
poetry run python examples/sorting_benchmark.py
```

## 4. Running Tests

To run tests with PyTest:

```bash
# Run all tests
poetry run pytest

# Run specific tests
poetry run pytest tests/algorithms/sorting/test_quick_sort.py
```

## 5. Adding New Algorithms

1. Create a new Python file in the appropriate directory:
   ```bash
   touch py_algo_study/algorithms/search/binary_search.py
   ```

2. Implement your algorithm

3. Create tests:
   ```bash
   mkdir -p tests/algorithms/search
   touch tests/algorithms/search/test_binary_search.py
   ```

## 6. Managing Dependencies

To add new packages:

```bash
# Add production dependencies
poetry add numpy

# Add development dependencies
poetry add --dev black
```

## 7. Maintaining Code Quality

For code formatting and quality checks:

```bash
# Format with Black
poetry run black .

# Sort imports with isort
poetry run isort .

# Lint with flake8
poetry run flake8
```
