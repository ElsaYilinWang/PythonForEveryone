# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

name = input("Hi, what's your name? ")
hours = float(input("How many hours do you work? "))
rate = float(input("What's your pay rate? "))
pay = hours * rate

print(f"Hello {name}, your gross pay is {pay} euros.")

