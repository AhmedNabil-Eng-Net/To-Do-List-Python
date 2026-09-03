def again():
    answer=input("Continue! y or n?").lower()
    while answer not in ("y", "n"):
        answer=input("Plz choose: y or n").lower()
    if answer=="n":
        print("Exiting..")
        return False
    return True
    
def show_tasks(tasks):
    if not tasks:
        print("The list is empty!")
        return
    print("📒 Tasks are:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}- {task}")
    
#------------------------Main Function-----------------------#

print(" Welcome to the To-Do list App ".center(52,"-"))
tasks=[]
loop=True
print("Choose an Option: ")
print("1. Add Task")
print("2. View Tasks")
print("3. Delete Task")
print("4. Exit")
print("".center(52,"-"))
while loop:
    try:
        choice=int(input("Your choice: "))
        if 1<= choice <=4:
            if choice==1:
                add_task=input("Enter the Task: ")
                tasks.append(add_task)
                print("the task is added✅")
            elif choice==2:
                show_tasks(tasks)               
            elif choice==3:
                show_tasks(tasks)
                if tasks:
                    del_task=int(input("which one to delete? "))
                    if del_task not in range (1,len(tasks)+1) :
                        print("Invalid task number!")
                    else:
                        print(f"task number: {del_task}.\"{tasks[del_task-1]}\" is deleted 🗑")
                        tasks.pop(del_task-1) # // del(Tasks[delTask])
                        show_tasks(tasks)
            else:
                print("Exiting..")
                break
            loop=again()
            
        else: print("Wrong choice. Please choose between 1 and 4!")
    except ValueError: print("Please choose a number!")
print("The Program is Closed!")
