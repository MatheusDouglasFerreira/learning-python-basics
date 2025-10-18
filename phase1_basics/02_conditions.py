# 02_conditions.py
# This script demonstrates conditional statements (if, elif, else) in Python.

age = int(input("Enter your age: "))

if age < 12:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

# Challenge: handle invalid input
try:
    age_check = int(input("Enter your age again: "))
    if age_check < 0:
        print("Age cannot be negative!")
except ValueError:
    print("Please enter a valid number!")
