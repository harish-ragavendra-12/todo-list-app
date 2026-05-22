# To-Do List Application using Python and JSON

A beginner-friendly command-line To-Do List application built using Python. This project allows users to manage tasks through CRUD operations (Create, Read, Update, Delete) and stores data permanently using a JSON file.

## Features

- Add multiple tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Stores task data in `tasks.json`
- Automatically creates `tasks.json` if it doesn't exist
- Input validation for better user experience

---

## Technologies Used

- Python
- JSON
- File Handling
- Lists
- Dictionaries
- Exception Handling

---

## Project Structure

```text
to_do_app/
│
├── main.py
├── tasks.json
└── README.md
```

---

## Task Data Format

Tasks are stored in JSON format:

```json
[
    {
        "task_id": 1,
        "task_name": "Learn PostgreSQL",
        "status": "Pending"
    },
    {
        "task_id": 2,
        "task_name": "Practice Python",
        "status": "Done"
    }
]
```

---

## Application Menu

```text
Menu
----------------
1. Add Tasks
2. View Tasks
3. Delete Tasks
4. Edit Tasks
5. Mark Complete
6. Exit
```

---

## How It Works

### Add Task
Users can enter one or multiple tasks. Tasks are stored with:

- Task ID
- Task Name
- Status

Default status:

```text
Pending
```

---

### View Tasks

Displays all available tasks and their current status.

Example:

```text
1. Learn PostgreSQL [Pending]
2. Practice Python [Done]
```

---

### Edit Tasks

Allows users to update an existing task.

Example:

```text
Learn SQL --> Learn PostgreSQL
```

---

### Delete Tasks

Removes selected tasks from the list and updates the JSON file.

---

### Mark Complete

Updates task status:

```text
Pending → Done
```

---

## Error Handling

The application handles:

- Invalid numeric input
- Empty task names
- Missing JSON file

---

## Future Improvements

- Add PostgreSQL database integration
- Add task priorities
- Add due dates
- Search tasks
- Filter completed/pending tasks
- Build GUI using Tkinter
- Convert into a Flask web application

---

## Learning Outcomes

This project helped me understand:

- Python functions
- Lists and dictionaries
- File handling
- JSON operations
- CRUD functionality
- Exception handling
- Project structure

---

## Author

Harish Ragavendra