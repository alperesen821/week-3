number = int(input("Enter an integer: "))
if number <=1:
    print(f"{number} is not a prime number.")
else:
    divisor = 2
    is_prime = True
    while divisor**2 <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")