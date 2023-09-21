# def greet_with(name, location):
#     print(f"Hello my name is {name}?")
#     print(f"This is my location {location}?")
#
#     greet_with("vikrez", "warristreet")


# Write your code below this line 👇
def prime_checker(number):
    """this is a prime checker, docstrings by victor"""
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
            if is_prime:
                print("It's is a prime number.")
            else:
                print("it's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)





