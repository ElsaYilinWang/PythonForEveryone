# Rewrite your pay computation to give the employee 1.5 times
# the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = float(input("Hi, how long have you worked in hours? "))
rate = float(input("What's the hourly rate? "))
pay = hours * rate

if hours > 40.0:
    pay = (hours - 40.0) * rate * 1.5 + 40.0 * rate

print(f"Your pay is {pay}.")