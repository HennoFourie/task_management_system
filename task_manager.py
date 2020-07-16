# Capstone Project 4
# Henno Fourie, 27/05/2020
# Create a program that will manage tasks assigned to each team member.

import sys # Allows you to use the sys.exit command to quit/logout of the application
from datetime import date # Importing datetime modules
import datetime
import os.path # Importing pathname modules


def reg_user(): # Function to registed new users
    duplicate = False
    while duplicate == False:
        print("\nRegister new user - \n")
        with open('user.txt','r') as userdata:
            # Request user to enter new username
            regUser = input("Enter new username: ")
            for line in userdata:
                list = line.split(', ')
                # If stattement will check if user didnt enter any duplicate usernames already registered.
                if regUser == list[0]:
                    print("Username already registered. Please try another username. ")
                    duplicate = False
                else:
                    # User will only be able to continue if username is unique
                    duplicate = True
    match = False
    while match == False:
        regPword = input("Enter new password: ")
        # Requesting user to re-enter the password
        # If statement will check if password is the same as first password input
        checkPword = input("Re-enter the password: ")
        if regPword == checkPword:
            # If password is correct, the login data will be saved in a file
            print("New user added. ")
            userdata = open('user.txt','a')
            userdata.write("\n" + regUser + ", "+ regPword)
            match = True
        else:
            # If password is not correct, user will be directed to menu
            print("Passwords does not match. Please try again. ")
            match = False
    userdata.close() # Close file when done
    

def add_task(): # Function to add new tasks
    print("\nAssign new task - \n")
    # Requesting input from user
    taskUser = input("Assign username to task: ")
    taskTitle = input("Enter a title of the task: ")
    taskDesc = input("Enter a description of the task: ")
    # Current date will be calculated
    taskDate = (date.today()).strftime("%d %b %Y")
    taskDue = input("Enter the due date of the task (format 01 Jan 2020): ")
    taskComp = "No"
    # After all the input is received, the task data will be saved in a file
    taskdata = open('tasks.txt','a')
    # The task data should be ordered in a certain order
    taskdata.write('\n{}, {}, {}, {}, {}, {}'.format(taskUser,taskTitle,taskDesc,taskDate,taskDue,taskComp))
    taskdata.close() # Close file when done
    print("New task added. ")


def view_all(): # Function to view all task
    print("\nDisplaying all the tasks - \n")
    # Open file to read all the task data
    taskdata = open('tasks.txt','r')
    for line in taskdata:
        # For each line, the data should be split, and printed out to the user
        list = line.split(', ')
        print("Task title: \t" + list[1] + "\nDescription: \t" + list[2] + "\nAssigned to: \t" + list[0] +
              "\nDate assigned: \t" + list[3] + "\nDue date: \t" + list[4] + "\nCompleted: \t" + list[5])
    taskdata.close() # Close file when done


def load_tasks(): # Function to load all tasks into dictionary (nested)
    task_indexes = {} # Create an empty dictionary variable to store indexes to tasks
    task_dict = {} # Declare an empty task dictionary to store task details
    index = 1 # Initialize an index variable to 1, to keep track of task numbers
     
    task_file = open("tasks.txt") # Open the tasks.txt file
    # Using a for loop staement to go through the lines in the tasks file
    for line in task_file:
            # check if the task_dict is empty:
            if task_dict:
                task_indexes[index] = task_dict
                index += 1
                task_dict = {}
                 
            task_key = index
            task_value = line.strip()
            task_dict[task_key] = task_value

    task_indexes[index] = task_dict
    task_file.close()
    return task_indexes

def load_task_dict(): # Function to load all tasks into dictionary
    task_dict = {}
    index = 1

    task_file = open("tasks.txt")

    for line in task_file:
        task_key = index
        task_value = line.strip()
        task_dict[task_key] = task_value
        index += 1

    task_file.close()
    return task_dict

def rewrite_tasks(task_dict): # Function to rewrite tasks to file after editing
    task_file = open('tasks.txt', 'w+') # Open the tasks.txt file
    count = 1 # Initialize an index variable to 1, to keep track of index in list
    for task in task_dict.values():
        for key, value in task.items():
            for word in value.split(", "):
                if count == 6:
                    # If count is equal to 6, then only the task will rewrite to file
                    task_file.write(word)
                else:
                    # If count is not 6, ',' will be added till count is 6
                    task_file.write(word + ", ")
                count += 1
        task_file.write("\n")
    print(task_file.read())
    task_file.close() # Close file when done
    
def view_mine(username): # Function to view all 'own' tasks, and edit selected task
    print("\nDisplaying all your tasks - \n")
    # Open file to read all the task data
    taskdata = open('tasks.txt','r')
    taskcount = 0
    for line in taskdata:
        taskcount += 1
        # For each line, the data should be split
        list = line.split(', ')
        # Using an if statement to only print current users tasks
        if username == list[0]:
            print("Task number: \t" + str(taskcount) + "\nTask title: \t" + list[1] + "\nDescription: \t" + list[2] + "\nDate assigned: \t"
                  + list[3] + "\nDue date: \t" + list[4] + "\nCompleted: \t" + list[5])
    taskdata.close() # Close file when done

    # Using a while loop statement with editing of task
    editTask = False
    while editTask == False:
        selection = input("\nPlease enter the spesific task number you would like to edit, or enter -1 to return to the main menu: ")

        if selection == "-1":
            # User will only return to main menu if -1 is entered.
            editTask = True
            break

        task_key = int(selection)
        print("""\nPlease selection one of the following options:
c - mark the task as complete
u - change the username assigned to the task
d - change the due date of the task \n""")
    
        def _edit_file(): # Function for marking task as complete
            task_dict = load_tasks()
            if task_key in task_dict.keys():
                selected_task = task_dict[task_key][task_key].strip().split(", ")
                # Task can only be edited if no complete
                if selected_task[5] != 'Yes':
                    selected_task[5] = 'Yes'
                    new_task = ""
                    for word in selected_task:
                        new_task += word.strip() + ", "
                    new_task.strip(", ")
                    task_dict[task_key][task_key] = new_task
                    rewrite_tasks(task_dict)
                    print("Task marked as completed. ")
                else:
                    print("Task already completed. No editing allowed. ")
            else:
                print("The task number is incorrect. ")
     
        def _edit_user(): # Function to edit username
            task_dict = load_tasks()
            if task_key in task_dict.keys():
                selected_task = task_dict[task_key][task_key].strip().split(", ")
                # Task can only be edited if no complete
                if selected_task[5] != "Yes":
                    selected_task[0] = input("Enter new username assigned to the task: ")
                    new_task = ""
                    for word in selected_task:
                        new_task += word.strip() + ", "
                    new_task.strip(", ")
                    task_dict[task_key][task_key] = new_task
                    rewrite_tasks(task_dict)
                    print("Username updated. ")
                else:
                    print("Task already completed. No editing allowed. ")
            else:
                print("The task number is incorrect. ")
            
        def _edit_date(): # Function to edit due date
            task_dict = load_tasks()
            if task_key in task_dict.keys():
                selected_task = task_dict[task_key][task_key].strip().split(", ")
                # Task can only be edited if no complete
                if selected_task[5] != "Yes":
                    due_date = input("Enter the new due date of the task (format 01 Jan 2020): ")
                    selected_task[4] = due_date
                    new_date = ""
                    for word in selected_task:
                        new_date += word.strip() + ", "
                    new_date.strip(", ")
                    task_dict[task_key][task_key] = new_date
                    rewrite_tasks(task_dict)
                    print("Due date updated. ")
                else:
                    print("Task already completed. No editing allowed. ")
            else:
                print("The task number is incorrect. ")

        # Based on users input, will lead user to the different editing functions
        editTask = input("Enter your selection: ").lower()
        if editTask == "c":
            _edit_file()
            editTask = False
        elif editTask == "u":
            _edit_user()
            editTask = False
        elif editTask == "d":
            _edit_date()
            editTask = False
        else:
            print("Selection no valid. Please try again. ")
            editTask = False


def reports_tasks(): # Function to generate tasks report
    task_dict = load_task_dict()
    total_tasks = len(task_dict) # Count total task in dictionary

    # For loop statement to count all the completed tasks
    completed = 0
    for task in task_dict.values():
        list = task.strip().split(',')
        if list[5] == "Yes" or list[5] == " Yes":
            completed += 1

    uncompleted = total_tasks - completed

    percentage_incomplete = int((uncompleted / total_tasks)*100)

    # For loop statement to count all the overdue tasks
    overdue = 0
    today = (date.today()).strftime("%d %b %Y")
    for task in task_dict.values():
        list = task.strip().split(',')
        if list[5] == "No" or list[5] == " No":
            due_date = list[4].strip()
            # String date converted back to date format to be able to do calculation
            test_due = datetime.datetime.strptime(due_date,"%d %b %Y").strftime("%d %b %Y")
            if test_due < today:
                overdue += 1
            
    percentage_overdue = int((overdue / total_tasks)*100)

    # Combine report to print to file
    report = ("Total tasks: "+str(total_tasks)+", Completed tasks: "+str(completed)+", Uncompleted tasks: "+str(uncompleted)+
    ", Uncompleted tasks & overdue: "+str(overdue)+", Percentage tasks incomplete: "+str(percentage_incomplete)+
    ", Percentage tasks overdue: "+str(percentage_overdue))
    return report

    
def reports_users(): # Function to generate tasks report
    task_dict = load_task_dict()
    # Opening userfile to count how many users
    with open('user.txt','r') as user_file:
        # Save user names in list to for data per user
        userlist = []
        for line in user_file:
            list = line.strip().split(', ')
            userlist.append(list[0])

    total_users = len(userlist) # Count total names in list
    total_tasks = len(task_dict) # Count total task in dictionary

    # While loop statement to count amount of tasks per username
    i = 0
    total_tasks_user = 0
    tasklist = []
    while i < total_users:
        total_tasks_user = 0
        for task in task_dict.values():
            list = task.strip().split(',')
            if list[0] == userlist[i]:
                # For each task matched with username, index will +1
                total_tasks_user += 1
            elif list[0] != userlist[i]:
                total_tasks_user += 0
        # Append result in list
        tasklist.append([userlist[i],": ",total_tasks_user])
        i += 1

    # While loop statement to count amount of completed tasks per username     
    i = 0
    tasklist_completed = []
    while i < total_users:
        complete = 0
        for task in task_dict.values():
            list = task.strip().split(',')
            if list[0] == userlist[i] and (list[5] == "Yes" or list[5] == " Yes"):
                # For each task matched with username and if task is completed, index will +1
                complete += 1
            elif list[0] != userlist[i]:
                complete += 0
        # Append result in list
        tasklist_completed.append([userlist[i],": ",complete])
        i += 1

    # Using a while loop to run through all the usernames, to append all data in a list
    i = 0
    report_per_user = []
    while i < total_users:
        username = userlist[i]
        totaltasks = tasklist[i][2]
        percentage_assigned = int((totaltasks / total_tasks)*100)
        totalcomp = tasklist_completed[i][2]
        percentage_completed = int((totalcomp / totaltasks)*100)
        percentage_uncompleted = int(100)- percentage_completed
        
        report_per_user.append("Username: "+str(username)+", Total tasks: "+str(totaltasks)+", Percentage of total tasks: "
                           +str(percentage_assigned)+", Percentage of completed: "+str(percentage_completed)+
                           ", Percentage of uncompleted: "+str(percentage_uncompleted))
        i += 1
    # Combine report to print to file
    report = ("Total users: "+str(total_users)+", Total tasks: "+str(total_tasks)+", "+str(report_per_user))
    return report


def statistics(): # Function to display statistics 
    print("\nDisplaying all the statistics - \n")

    print("Task overview - ")
    f = open('task_overview.txt','r') # Open file to read date    
    for line in f:
        list = line.strip().split(', ')
    f.close()
    
    #Print data to user
    print('{}\n{}\n{}\n{}\n{}\n{}'.format(list[0],list[1],list[2],list[3],list[4],list[5]))    

    print("\nUser overview - ")
    f = open('user_overview.txt','r') # Open file to read date    
    for line in f:
        list = line.strip().split(', ')
    f.close()
    #Print data to user
    print(*list,sep = "\n")


# Create while loop statement to request username & password
# Username & password should be looked up in a txt file
# If data found, user can continue with program
# If no login data found, user cannot log in

found = False
while found == False:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Open file containing username & passwords
    with open('user.txt','r') as userdata:
        for line in userdata:
            if (username + ", " + password) == line.strip():
                # If login data is the same as in file, user will be able to continue
                print("\nYou are logged in! ")
                found = True
                userdata.close() # Close file when done
                break
        if not found:
            # If login data is not found, user will receive a message to try again
            print("Incorrect username or password entered. Please try again. \n")
            found = False

# Program created on a while loop statement
# User will make a selection from the menu to be directed to the certain module

choice = ''
while choice != "e":
    # Print menu to user to select from
    if username == "admin":
        # Admin have an additional selection
        print("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit \n""")
    else:
        # Print menu to user to select from
        print("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit \n""")

    # Request input from user, after each if statement, the user will be directed back to menu
    choice = input("Enter your selection: ").lower()

    # If user select to register a new user
    if choice == "r":
        # Only the admin user can use this module
        if username == "admin":
            reg_user()
        else:
            # All other users will receive the error message
            print("Not authorised. ")

    # If user select to add a task
    elif choice == "a":
        add_task()

    # If user select to view all task
    elif choice == "va":
        view_all()

    # If user select to view only their tasks
    elif choice == "vm":
        view_mine(username)

    # If user select to view the statistics
    elif choice == "gr":
        # Only the admin user can user this module
        if username == "admin":
            # Create new file, and print report to file
            f = open("task_overview.txt", "w+")
            f.write(reports_tasks())
            f.close()
            # Create new file, and print report to file
            f = open("user_overview.txt", "w+")
            f.write(reports_users())
            f.close()

            print("Reports generated. ")

    # If user select to view the statistics
    elif choice == "ds":
        # Only the admin user can user this module
        if username == "admin":
            # If file not found, user need to generate reports first
            if os.path.isfile('task_overview.txt') != True:
                print("No data found, please generate reports. ")
            # If file not found, user need to generate reports first
            elif os.path.isfile('user_overview.txt') != True:
                print("No data found, please generate reports. ")
            else:
                statistics()
            
    # If user select to exit
    elif choice == "e":
        print("\nYou have logged out.")
        sys.exit
