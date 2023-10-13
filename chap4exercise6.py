# Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters.
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
    """
    This function takes 2 parameters: hours and rate
    if work hours > 40, then the rate * 1.5
    computepay(45, 10)
    475.0
    """

    if hours > 40.0:
        pay = (hours - 40.0) * rate * 1.5 + 40.0 * rate

    pay = hours * rate
    print(f"Your pay is {pay}.")

computepay(45, 10)