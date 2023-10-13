# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

total = 0
count = 0
num_list = []

user_input = input("Enter a number or 'done': ")

while user_input != "done":
    try:
        num = int(user_input)
        total = total + num
        count += 1
        num_list.append(num)

    except:
        print("Please enter a valid number or 'done'!")

    user_input = input("Enter a number or 'done': ")


print(f"{count} numbers,  max is {max(num_list)} and min is {min(num_list)}")