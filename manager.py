import time
import datetime
import item

class Manager(object):

# Print all of the items on the to-do list:
    def printlist():
        # Print all of the items on the to-do list:
        f = open('todos.txt', 'r') # (file, action)  this opens todo.txt in read('r') mode and assigns it to the variable f.

        list = f.read() # .read() reads the file assigned to the variable f.  this is assigned to message.  So the read file = message.

        print(list) # print the value of message.  so print the read file.
        f.close() # close the file since we are done with it.

# Add a new item with timestamp to the to-do list:
    def addtask():
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # add timestamp from imported modules
        file1 = open('todos.txt', 'a+') # (file, action)  this opens todo.txt in append('a+') mode and assigns it to the variable file1.
        task = input("Create A New Task: ") # the user will see the string 'Create A New Task: ' which is followed by the user's input.  Assign the user's input to task.
        file1.write("\n" + task + ' ' + now) # add task on a new line to file1, which would be todos.txt in this case.
        file1.close() # close file1, todos.txt in this case.


# Mark an item as complete:
    def completed():
        edit = open('todos.txt').read() # assign edit to todos.txt and read it

        taskcomplete = input('What task did you complete? ') # ask for user task

        markedtask = edit.replace(taskcomplete, taskcomplete + " COMPLETED " + str(True)) # replace taskcomplete with taskcomplete + the string COMPLETE

        f2 = open('todos.txt', 'w+') # open the file in write mode
        if f2 == markedtask: # if the completed task != the name of the input
            f2.write(markedtask) # return
        else:
            print('You don\'t have that task.')
        f2.write(markedtask) # actually add "taskcomplete + COMPLETE" to the file
        f2.close() # closesd the file
        f = open('todos.txt', 'r') # open todos.txt in read mode
        message = f.read() # assign message to the updated file in read mode
        print(message) # print the list
        f.close() # close the updated files

Manager.printlist()
Manager.addtask()
Manager.completed()
