# To-Do List Manager using Python List Methods with Colorama

from colorama import Fore, Style, init
init(autoreset=True)  # Initialize Colorama for automatic reset

tasks = []  # Empty list to store tasks

def add_task(task):
    """Add a task to the list."""
    tasks.append(task)
    print(Fore.GREEN + f'✅ Task "{task}" added!')

def remove_task(task):
    """Remove a task from the list."""
    if task in tasks:
        tasks.remove(task)
        print(Fore.RED + f'❌ Task "{task}" removed!')
    else:
        print(Fore.YELLOW + f'⚠️ Task "{task}" not found!')

def view_tasks():
    """Display all tasks."""
    if tasks:
        print(Fore.CYAN + "\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(Fore.LIGHTMAGENTA_EX + f"{i}. {task}")
    else:
        print(Fore.YELLOW + "📭 Your To-Do List is empty!")

def sort_tasks():
    """Sort tasks in alphabetical order."""
    tasks.sort()
    print(Fore.BLUE + "🔤 Tasks sorted alphabetically!")

def find_task(task):
    """Find if a task exists in the list."""
    if task in tasks:
        index = tasks.index(task)
        print(Fore.GREEN + f'🔍 Task "{task}" found at position {index + 1}')
    else:
        print(Fore.RED + f'❌ Task "{task}" not found!')

def count_task(task):
    """Count occurrences of a task in the list."""
    count = tasks.count(task)
    print(Fore.MAGENTA + f'🔢 Task "{task}" appears {count} time(s) in the list.')

def clear_tasks():
    """Clear all tasks from the list."""
    tasks.clear()
    print(Fore.RED + "🗑️ All tasks cleared!")

# 🚀 Running the To-Do List Manager
while True:
    print(Fore.YELLOW + "\n📌 MENU 📌")
    print(Fore.CYAN + "1️⃣ Add Task")
    print(Fore.CYAN + "2️⃣ Remove Task")
    print(Fore.CYAN + "3️⃣ View Tasks")
    print(Fore.CYAN + "4️⃣ Sort Tasks")
    print(Fore.CYAN + "5️⃣ Find Task")
    print(Fore.CYAN + "6️⃣ Count Task")
    print(Fore.CYAN + "7️⃣ Clear All Tasks")
    print(Fore.CYAN + "8️⃣ Exit")

    choice = input(Fore.LIGHTWHITE_EX + "Enter your choice (1-8): ")

    if choice == "1":
        task = input(Fore.LIGHTGREEN_EX + "Enter a task: ")
        add_task(task)
    elif choice == "2":
        task = input(Fore.LIGHTRED_EX + "Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        sort_tasks()
    elif choice == "5":
        task = input(Fore.LIGHTBLUE_EX + "Enter task to find: ")
        find_task(task)
    elif choice == "6":
        task = input(Fore.LIGHTMAGENTA_EX + "Enter task to count: ")
        count_task(task)
    elif choice == "7":
        clear_tasks()
    elif choice == "8":
        print(Fore.LIGHTYELLOW_EX + "👋 Exiting... Goodbye!")
        break
    else:
        print(Fore.RED + "⚠️ Invalid choice! Please enter a number between 1-8.")
