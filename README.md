# Algorithm Study Project

This repository is for learning algorithms and data structures using Python.

## Setup

1. Install Poetry (if you haven't already):
   ```bash
   pip install poetry
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Project Structure

- `py_algo_study/`: Main source code directory
  - `data_structures/`: Implementations of various data structures
  - `algorithms/`: Algorithm implementations
  - `utils/`: Utility functions
- `tests/`: Test code
- `examples/`: Algorithm usage examples

## How to Run

```bash
# Example: Run a sorting algorithm
poetry run python -m py_algo_study.algorithms.sorting.quick_sort
```
