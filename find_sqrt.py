given_number = int(input("Enter an integer: "))
if given_number < 0:
    print("The square root of a negative number is not defined in the set of real numbers.")
else:
    guess_number = 0
    while guess_number**2 < given_number:
        guess_number += 1
    if guess_number**2 == given_number:
        print(f"Square root of {given_number} is {guess_number}.")
    else:
        print(f"{given_number} is not a perfect square.")