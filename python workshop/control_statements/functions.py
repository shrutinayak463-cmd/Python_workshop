name=input("Enter ur name: ")
def greet():
    print("Hello !" +name)

greet()

num=int(input("Enter a number: "))
def add(num):
    print(num)

add(num)


def username():
    return "Arjun"

print(username())




age=int(input("Enter a age: "))
def valid(age):
    if(age>=18):
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
valid(age)
