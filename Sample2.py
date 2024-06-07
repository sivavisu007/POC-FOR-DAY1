# Define a function to perform the calculation
def addition(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    return x / y


#Printing the avaliable option to the user

print("select operation")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Division")
#using while loop to perform the calculation and continuous the program without restarting the program
while True:
    #get the using input for calculation
    option = input("enter which operation do you want(1,2,3,4):")
    if option in ("1", "2", "3", "4"):
        #using try and except for if user mistakenly type letters instead of number, it will help with that without restarting the program
        try:
            num1 = float(input("enter the first number"))
            num2 = float(input("enter the second number"))
        except ValueError:
            print("Invalid input, please enter positive number")
            continue
        if option == "1":
            print(addition(num1, num2))
        elif option == "2":
            print(subtract(num1, num2))
        elif option == "3":
            print(multiply(num1, num2))
        elif option == "4":
            print(division(num1, num2))
            #get the user input for him/her wants to continue the program or not
        next_cal = input("if you want to continue? Then type[YES/NO]:")
        if next_cal == "no":
            print("Thank you")
            break
        else:
            print("Select operation")