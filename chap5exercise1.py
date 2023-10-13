# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number,
# detect their mistake using try and except and print an error message
# and skip to the next number.

total = 0
count = 0

user_input = input("Enter a number or 'done': ")

while user_input != "done":
    try:
        num = int(user_input)
        total = total + num
        count += 1

    except:
        print("Please enter a valid number or 'done'!")

    user_input = input("Enter a number or 'done': ")


print(f"{count} numbers, sum is {total}, average is {total/count}")
