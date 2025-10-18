# Phase 1: Python Basics

This folder contains my first exercises while learning Python.
The goal is to understand how to use variables, conditions, lists, and dictionaries.

## Topics covered
- Variables and data types
- User input
- Conditional statements (`if`, `elif`, `else`)
- Lists and dictionaries
- Loops (`for`, `while`)

## Example
```python
clients = []

for i in range(1, 4):
    clients.append({
        'name': input(f"Enter the name of person {i}: "),
        'age': int(input(f"Enter the age of person {i}: "))
    })

for client in clients:
    print(f"Name: {client['name']}, Age: {client['age']}")

