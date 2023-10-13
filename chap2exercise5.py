# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit,
# and print out the converted temperature.

c_temp = float(input("Hi, what's the Celsius temperature? "))
f_temp = c_temp * 9/5 + 32
print(f"The temperature is {c_temp} Celsius degree, which is {f_temp} Fahrenheit degree.")
