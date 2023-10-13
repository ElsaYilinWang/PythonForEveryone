# Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    hours = float(input("Hi, how long have you worked in hours? "))
    rate = float(input("What's the hourly rate? "))
    pay = hours * rate
except:
    print("Error, please enter numeric input!")