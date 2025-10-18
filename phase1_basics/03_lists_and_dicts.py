# 03_lists_and_dicts.py
# This script demonstrates how to use lists, dictionaries, and loops in Python.

# Create an empty list to store clients
clients_list = []

# Add 3 clients with name and age
for i in range(1, 4):
    name = input(f"Enter the name of person {i}: ")
    age = int(input(f"Enter the age of person {i}: "))
    client = {'name': name, 'age': age}
    clients_list.append(client)

# Print all clients
print("\nList of clients:")
for client in clients_list:
    print(f"Name: {client['name']}, Age: {client['age']}")

# Challenge: print only clients older than 18
print("\nClients older than 18:")
for client in clients_list:
    if client['age'] > 18:
        print(f"Name: {client['name']}, Age: {client['age']}")
