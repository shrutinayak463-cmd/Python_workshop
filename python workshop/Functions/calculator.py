def userInput():
    first_input=int(input("Enter the first number :"))
    second_input=int(input("Enter the second number : "))
    return first_input,second_input


def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def multi(a=0,b=0):
    return a*b


print("Welcome to cal")
while True:
    print("Select the option :\n 1:Add\n 2:Sub\n 3.Multi\n 4.stop")
    option=int(input("Enter the option :"))

    if option==1:
        x,y=userInput()
        print(f"Addition of two numbers : {add(x,y)} ")

    elif option==2:
        x, y = userInput()
        print(f"Subtraction of two numbers : {sub(x,y)} ")


    elif option == 3:
        x, y = userInput()
        print(f"Multiplication of two numbers : {multi(x, y)} ")

    elif option == 4:
        print("Thanks for using calculator! ")

