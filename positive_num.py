# define usernumber
# request user input
# validate whether input his a number.

user_no = input("Enter your number : ")
 
try:

    user_no = float(user_no)
    print("hooray this is number")

    if user_no >= 0:
        print("you entered a positive number")
    elif user_no < 0:
        print("The number entered is not positive")

except:
        print("This is not a number")

