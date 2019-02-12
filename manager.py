import time
import datetime
import item
from textwrap import dedent

class Manager(object):

    print('\nWelcome to your Todo Manager!') # welcome message

    def welcome(): # function for input options
        print(dedent("""
            What would you like to do?
            1. Add a task.
            2. Complete a task.
            3. Show list.
            4. Quit.
            """))

        choice = input('> ') # assign choice to the user's input options lines 21 - 37

        if choice == '1' or choice == 'add a task' or choice == 'add task' or choice == 'add': # user input options to run addtask() to add a task to the todo list
            Manager.addtask() # from class Manager, get/run funciton addtask()

        elif choice == '2' or choice == 'complete a task' or choice == 'complete task' or choice == 'complete': # user input optioms to run complete() to mark a task as COMPLETED
            Manager.completed() # from class Manager, get/run completed()

        elif choice == '3' or choice == 'show list' or choice == 'show' or choice == 'list': # user input options to run printlist() to print all of the tasks/completed tasks on the to do list
            Manager.printlist() # form class Manager, get/run printlist()
            Manager.welcome() # from class Manager, get/run welcome()

        elif choice == '4' or choice == 'quit' or choice == 'q' or choice == 'bounce': # user input options to quit the program
            print('\nGoodbye!\n') # print Goodbye!
            exit(0) # exit program

        else:
            print("\nType something else.\n")
            Manager.welcome() # from class Manager, get/run welcome()

# Print all of the items on the to-do list:
    def printlist():

        f = open('todos.txt', 'r') # (file, action)  this opens todo.txt in read('r') mode and assigns it to the variable f.

        list = f.read() # .read() reads the file assigned to the variable f.  this is assigned to list.  So the read file = list.

        print(list) # print the value of list.  so print the read file.
        f.close() # close the file since we are done with it.

# Add a new item with timestamp to the to-do list:
    def addtask():

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # add timestamp from imported modules and format it so it does not say miliseconds

        file1 = open('todos.txt', 'a+') # (file, action)  this opens todo.txt in append('a+') mode and assigns it to the variable file1.
        task = input('Create A New Task: ') # the user will see the string 'Create A New Task: ' which is followed by the user's input.  Assign the user's input to task.

        file1.write("\n" + task + ' ' + now) # add task on a new line to file1, which would be todos.txt in this case.
        file1.close() # close file1, todos.txt in this case.
        print('\nTask Added!\n')

        Manager.welcome()

# Mark an item as complete:
    def completed():
        edit = open('todos.txt').read() # assign edit to todos.txt and read it

        taskcomplete = input('What task did you complete? ') # ask for user task

        markedtask = edit.replace(taskcomplete, taskcomplete + ' COMPLETED ' + str(True)) # replace taskcomplete with taskcomplete + the string COMPLETE

        f2 = open('todos.txt', 'w+') # open the file in write mode

        f2.write(markedtask) # actually add "taskcomplete + COMPLETE" to the file
        f2.close() # closesd the file

        f = open('todos.txt', 'r') # open todos.txt in read mode
        message = f.read() # assign message to the updated file in read mode
        print(message) # print the list
        f.close() # close the updated files

        print('\nTask marked as Completed!\n')

        Manager.welcome()

Manager() # call class Manager
Manager.welcome() # call class Manager, then get/run welcome function.
