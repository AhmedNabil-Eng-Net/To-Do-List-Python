#```#
def again():
    # Ask the user if they want to continue
    answer = input("Continue! y or n?").lower()

    # Keep asking until the user enters only y or n
    while answer not in ("y", "n"):
        answer = input("Plz choose: y or n").lower()

    # If the user chooses n, return False to stop the main loop
    if answer == "n":
        print("Exiting..")
        return False

    # If the user chooses y, return True to continue the program
    return True


def show_tasks(tasks):
    # Check if the list is empty
    if not tasks:
        print("The list is empty!")
        return

    print("📒 Tasks are:")

    # enumerate() gives us both the task number and the task itself
    # start=1 makes the numbering begin from 1 instead of 0
    for i, task in enumerate(tasks, start=1):
        print(f"{i}- {task}")


# ------------------------# Main #-----------------------#

# Display the program title
print(" Welcome to the To-Do list App ".center(52, "-"))

# Create an empty list to store the tasks
tasks = []

# Control variable for the main while loop
loop = True

# Display the available options
print("Choose an Option: ")
print("1. Add Task")
print("2. View Tasks")
print("3. Delete Task")
print("4. Exit")
print("".center(52, "-"))


# Main program loop
while loop:
    try:
        # Get the user's choice and convert it from string to integer
        choice = int(input("Your choice: "))

        # Check that the choice is between 1 and 4
        if 1 <= choice <= 4:

            # ---------------- Add Task ----------------
            if choice == 1:

                # Get a new task from the user
                add_task = input("Enter the Task: ")

                # Add the task to the list
                tasks.append(add_task)

                print("The task is added✅")


            # ---------------- View Tasks ----------------
            elif choice == 2:

                # Call the function to display all tasks
                show_tasks(tasks)


            # ---------------- Delete Task ----------------
            elif choice == 3:

                # Show the current tasks before choosing one to delete
                show_tasks(tasks)

                # Only ask for a task number if the list contains tasks
                if tasks:

                    # Get the task number from the user
                    del_task = int(input("Which one to delete? "))

                    # Make sure the entered number matches an existing task number
                    if del_task not in range(1, len(tasks) + 1):
                        print("Invalid task number!")

                    else:
                        # -1 converts the user's number to Python's list index
                        # Example: task 1 -> index 0, task 2 -> index 1
                        print(
                            f'task number: {del_task}."{tasks[del_task - 1]}" is deleted 🗑'
                        )

                        # Remove the selected task from the list
                        tasks.pop(del_task - 1)

                        # Show the updated list after deletion
                        show_tasks(tasks)


            # ---------------- Exit ----------------
            else:

                # Exit the main loop and end the program
                print("Exiting..")
                break


            # Ask the user whether to continue or stop
            # again() returns True or False and stores the result in loop
            loop = again()


        else:
            # The user entered a number outside the allowed range
            print("Wrong choice. Please choose between 1 and 4!")

    except ValueError:
        # Handles non-numeric input when int() is used
        print("Please choose a number!")


# Final message after the main loop ends
print("The Program is Closed!")
#```#