# Project 2: To-Do List App
# Save tasks to file
# Read, delete, update tasks
# Track changes via git commit

def add1(task):
    with open("test.txt","w") as f:
        f.write(task + "\n")

def read1():
    with open("test.txt","r") as f:
        print(f.read())

def del1():
       open("test.txt","w").close()
        
while True:

    print("1. add task")        
    print("2. read task")        
    print("3 delete task")        
    print("4. Exit")        

    choice = int(input("Enter choice between(1-4): "))

    if choice == 1:
        task = input("enter your task: ")
        add1(task)      

    elif choice == 2:
        read1()   

    elif choice == 3:
        del1()    

    elif choice == 4:
        print("progarm done byy")
        break

    else:
        print("please enter valid choice")    
