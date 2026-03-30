# PawPal+ (Module 2 Project)

## Description
PawPal+ is a pet care management system designed to help pet owners organize and track daily care tasks such as feeding, walking, and medication. The system uses object-oriented programming and scheduling logic to manage tasks efficiently across multiple pets.

This project follows a CLI-first development approach, where the backend logic is tested in a Python script before being integrated into a Streamlit web application.

---

## Features

- Create and manage multiple pets
- Add and track pet care tasks
- Sort tasks by time
- Detect scheduling conflicts
- Mark tasks as complete
- Filter tasks by completion status or pet
- Basic recurring task support (daily/weekly)
- CLI demo for testing logic
- Streamlit UI for user interaction
- Automated tests using pytest

---

## Project Structure
pawpal_project/
│
├── app.py # Streamlit UI
├── main.py # CLI demo script
├── pawpal_system.py # Core backend logic
├── README.md # Project documentation
├── reflection.md # Project reflection
├── requirements.txt # Dependencies
└── tests/
└── test_pawpal.py # Pytest test suite


---

## How to Run

### 1. Run the CLI Demo

This tests the backend logic directly in the terminal: python main.py

---

### 2. Run the Streamlit App

Launch the web interface: streamlit run app.py

---

### 3. Run Tests

Run automated tests to verify functionality: python -m pytest

---

## Testing

This project includes a pytest test suite that verifies:

- Task completion functionality
- Adding tasks to pets
- Sorting tasks by time
- Conflict detection logic

All tests pass successfully, confirming that the core system behaves as expected.

---

## Smarter Scheduling

The Scheduler class includes basic algorithmic logic:

- Tasks are sorted using Python’s `sorted()` function
- Filtering allows users to view tasks by status or pet
- Conflict detection identifies tasks scheduled at the same time
- Recurring tasks generate new tasks when completed (daily/weekly)

---

## Confidence Level

⭐⭐⭐⭐☆

The system successfully implements core scheduling features including sorting, filtering, and conflict detection. While it does not handle complex overlapping time ranges, it performs reliably for the intended use case.

---

## Author

Arthur Nisbeth