import time
import datetime
import item

# the app keeps closing everytime a task is input or completed.  find why.


class Manager(object):

    def welcome():
        print('Welcome to your Todo Manager!')
        print('Would you like to do?')
        print('1. Add a task.')
        print('2. Complete a task.')
        print('3. Quit.')

        choice = input('> ')

        if choice == '1' or choice.lower() == 'Add a task' or choice.lower() == 'Add':
            Manager.addtask()

        elif choice == '2' or choice.lower() == 'Commplete a task' or choice.lower() == 'Complete':
            Manager.completed()

        elif choice == '3' or choice.lower() == 'Quit':
            print('Goodbye!')
            exit(0)

        else:
            print("Type something else.")

# Print all of the items on the to-do list:
    def printlist():

        f = open('todos.txt', 'r') # (file, action)  this opens todo.txt in read('r') mode and assigns it to the variable f.

        list = f.read() # .read() reads the file assigned to the variable f.  this is assigned to list.  So the read file = list.

        print(list) # print the value of message.  so print the read file.
        f.close() # close the file since we are done with it.

# Add a new item with timestamp to the to-do list:
    def addtask():
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # add timestamp from imported modules and fornat it so it does not say miliseconds
        file1 = open('todos.txt', 'a+') # (file, action)  this opens todo.txt in append('a+') mode and assigns it to the variable file1.
        task = input('Create A New Task: ') # the user will see the string 'Create A New Task: ' which is followed by the user's input.  Assign the user's input to task.
        file1.write("\n" + task + ' ' + now) # add task on a new line to file1, which would be todos.txt in this case.
        file1.close() # close file1, todos.txt in this case.


# Mark an item as complete:
    def completed():
        edit = open('todos.txt').read() # assign edit to todos.txt and read it

        taskcomplete = input('What task did you complete? ') # ask for user task

        markedtask = edit.replace(taskcomplete, taskcomplete + ' COMPLETED ' + str(True)) # replace taskcomplete with taskcomplete + the string COMPLETE

        f2 = open('todos.txt', 'w+') # open the file in write mode
        if f2 == markedtask: # if the completed task == the marked task
            f2.write(markedtask) # add COMPLETED to the task
        else:
            print('You don\'t have that task.')
        f2.write(markedtask) # actually add "taskcomplete + COMPLETE" to the file
        f2.close() # closesd the file
        f = open('todos.txt', 'r') # open todos.txt in read mode
        message = f.read() # assign message to the updated file in read mode
        print(message) # print the list
        f.close() # close the updated files

Manager.welcome()
