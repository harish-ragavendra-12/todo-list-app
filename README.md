# To Do List App 📝

A simple command-line based To Do List application built using Python.

This project allows users to manage tasks through a menu-driven interface. Users can add, view, edit, delete, and mark tasks as completed.

## Features

✅ Add multiple tasks  
✅ View all tasks with status  
✅ Edit existing tasks  
✅ Delete tasks  
✅ Mark tasks as completed  
✅ Input validation using try-except  
✅ Prevent empty task entries  

---

## Technologies Used

- Python
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling

---

## Project Structure

```text
todo-list-app/
│
├── todo.py
└── README.md
```

---

## Task Data Format

Each task is stored as a dictionary:

```python
{
    "task": "Learn Python",
    "status": "Pending"
}
```

Example after completion:

```python
{
    "task": "Learn Python",
    "status": "Done"
}
```

---

## Menu Options

```text
1. Add Tasks
2. View Tasks
3. Delete Tasks
4. Edit Tasks
5. Mark Complete
6. Exit
```

---

## Sample Output

```text
Menu
-----------------
1. Add Tasks
2. View Tasks
3. Delete Tasks
4. Edit Tasks
5. Mark Complete
6. Exit

Enter your choice: 1

How many tasks do you want to add? 2

Enter task 1: Learn Python
Enter task 2: Practice PostgreSQL

Tasks added successfully...


Tasks to be completed:

1. Learn Python [Pending]
2. Practice PostgreSQL [Pending]
```

---

## Learning Outcomes

This project helped practice:

- Functions
- List operations
- Dictionary usage
- Input validation
- Exception handling
- Building menu-driven applications
- Basic project structuring

---

## Future Improvements

- Save tasks using file handling
- Store tasks in PostgreSQL
- Add due dates
- Add task priorities
- Create GUI using Tkinter
- Build a web version using Flask

---

## Author

Harish Ragavendra