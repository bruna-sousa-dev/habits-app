# Habits App with Flet

## Overview

This project implements a simple habit tracking application built with **Python** and **Flet**, focused on **reactive interface behavior**, **dynamic state update**, and **real-time progress feedback**.

The application allows the user to:
- View a daily habits dashboard
- Mark habits as completed using checkboxes
- Track progress automatically through a progress bar and percentage indicator
- Add new habits dynamically through the input field
- Interact with a modern dark interface using gradients and clean visual composition

---

## Architecture

The application architecture is organized around **state-driven UI behavior**, even though it is implemented in a single `main.py` file.

### 1. Application Entry Point
- `ft.app(target=main, assets_dir="assets")`
- Flet initializes the application and injects the `page` object into the main function

### 2. Main Application Class
- `App(page)` encapsulates interface initialization and screen construction
- Global page properties such as title, padding, and background color are configured during initialization

### 3. State Management
- Habits are stored in a local list of dictionaries:
- `{"title": "...", "done": False}`
- This structure works as the application’s source of truth

### 4. Reactive Logic
- `change()` updates the completion state of habits
- Progress is recalculated every time a checkbox changes
- The UI is refreshed with `self.page.update()`

### 5. Dynamic UI Composition
- `rebuild_habits()` regenerates the checkbox list based on the current application state
- `add_habit()` validates input, mutates the state, rebuilds the list, and recalculates progress

### 6. Interface Layer
- Main vertical layout built with `ft.Column`
- Progress card built with `ft.Container`, `ft.Text`, and `ft.ProgressBar`
- Habit list area built with a scrollable `ft.Column`
- Input handled through `ft.TextField`
- Final composition added to the page through `self.page.add(layout)`

---

## Features

- Dynamic habit creation
- Real-time progress calculation
- Event-driven UI updates
- Scrollable habits list
- Gradient-based modern interface
- Input validation for empty habits
- Simple and readable state model
- Strong foundation for future backend or persistence integration

---

## Technologies

- Python
- Flet

---

## How it works

### Progress update flow
1. The user marks a checkbox
2. The `change()` function updates the corresponding item in `habits_list`
3. Completed habits are counted
4. Progress percentage is recalculated
5. `progress_text` and `progress_bar` are updated
6. The page is refreshed

### New habit insertion flow
1. The user types a habit in the input field
2. Pressing Enter triggers `add_habit()`
3. Input is sanitized and validated
4. A new item is appended to `habits_list`
5. The habits list is rebuilt
6. Progress is recalculated automatically

---

## Running the project

### Requirements
- Python 3.10+
- Flet installed

### Installation
```bash
pip install flet
```

### Execution
```bash
python main.py
```

---

## Possible next improvements

- Local data persistence
- Integration with SQLite or a REST API
- Authentication
- Daily / weekly tracking
- Responsive adaptation for mobile deployment
- Notification system
- Cloud synchronization

---

## License

This project is licensed under a Private License. All rights reserved to the author.

---

## Author

Developed by:

**Bruna Sousa**  
Electrical/Electronic Engineer specializing in Data Science and Artificial Intelligence  
GitHub: https://github.com/bruna-sousa-dev  
LinkedIn: https://www.linkedin.com/in/bruna-sousa-dev/

---

## Notes

- The project is intentionally simple and focused on interface experimentation and reactive behavior using Flet
- It is a strong base for studying state-driven applications in Python
