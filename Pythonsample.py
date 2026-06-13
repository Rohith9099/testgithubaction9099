# Initialize an empty list to store tasks
todo_list = []

def display_menu():
    """Prints the application menu choices to the user."""
    print("\n--- TO-DO LIST APP ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit Application")

def view_tasks():
    """Displays all current tasks in the list."""
    if not todo_list:
        print("\nYour to-do list is currently empty!")
    else:
        print("\nYour Current Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    """Prompts user and adds a new task to the list."""
    new_task = input("\nEnter the task description: ").strip()
    if new_task:
        todo_list.append(new_task)
        print(f"Success: '{new_task}' has been added.")
    else:
        print("Error: Task cannot be blank.")

def delete_task():
    """Deletes a task based on its number position."""
    view_tasks()
    if todo_list:
        try:
            choice = int(input("\nEnter the number of the task to delete: "))
            # Adjust for 0-based indexing
            removed_task = todo_list.pop(choice - 1)
            print(f"Removed: '{removed_task}' has been deleted.")
        except (ValueError, IndexError):
            print("Invalid Selection: Please enter a valid task number.")

def main():
    """Main application loop to run the program continuously."""
    while True:
        display_menu()
        user_choice = input("\nSelect an option (1-4): ").strip()
        
        if user_choice == "1":
            view_tasks()
        elif user_choice == "2":
            add_task()
        elif user_choice == "3":
            delete_task()
        elif user_choice == "4":
            print("\nThank you for using the application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

# Check if the script is run directly to start the program
if __name__ == "__main__":
    main()
