# Project 1: Basic Calculator
# Functions for addition, subtraction , etc.
# Loop menu for operations
# Error handling for invalid inputs

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def devied(a,b):

    if b==0:
        print("please enter valid value!")
        
    else:
        return a/b

# loop manu 
try: 

    while True:
        print("1. addition")        
        print("2. subtraction")        
        print("3. multiply")        
        print("4. devied")        
        print("5. Exit")    


        num1= int(input("Enter a number 1: "))
        num2= int(input("Enter a number 2: "))

        choice = int(input("Enrter a value between (1-5): "))

        if choice not in [1,2,3,4,5]:
            print("Please enter a valid value between(1-5)")

        elif choice == 1:
            print("Ans",add(num1,num2))    
        
        elif choice == 2:
            print("Ans",subtract(num1,num2))    

        elif choice == 3:
            print("Ans",multiply(num1,num2))    
            
        elif choice == 4:
            print("Ans",devied(num1,num2))    

        elif choice == 5:
            print("Good byy! thax ")    
            break

except ValueError:
    print("Please enter valid value")


         


