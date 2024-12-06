import random


def factorial(n):
    fct = 1
    for i in range(1, n + 1):
        fct = fct * i
    return fct


def solve_linear_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    x = -b / a

    return a, b, x


def is_prime(val):
    if val <= 1:
        return False
    if val == 2:
        return True
    if val % 2 == 0:
        return False
    for i in range(3, int(val ** 0.5) + 1, 2):
        if val % i == 0:
            return False
    return True


def nearest_prime(n):
    # Find the first prime number greater than or equal to n.

    while not is_prime(n):  # Keep checking numbers until a prime is found
        n += 1
    return n

"""
def math_roulette_challenge():

    global operation_sign, res
    nb = [random.randint(1, 20) for i in range(5)]

    operation = random.choice(['add', 'sub', 'mul',])

    if operation == "addition":
        res = sum(numbers)
        operation_sign = "+"
    elif operation == "subtraction":
        res = numbers[0]
        for num in numbers[1:]:
            res -= num
        operation_sign = "-"
    elif operation == "multiplication":
        result = 1
        for num in numbers:
            res *= num
        operation_sign = "*"

    nb_str = f' {operation_sign} '.join(map(str, nb))
    print(f"Calculate the result of: {nb_str}")

    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("invalid input. Please enter an integer.")
        return False

    if user_answer == res:
        print("correct! you win")
        return True
    else:
        print(f"invalid input. the correct answer was {res}. Better luck next time!")
        return False
"""


def math_roulette_challenge():
    """
    Math roulette game where the user calculates the result of a random operation
    applied to five random numbers and wins if their answer is correct.

    :return: True if the user's answer is correct, False otherwise.
    """
    # Generate 5 random numbers between 1 and 20
    numbers = [random.randint(1, 20) for _ in range(5)]

    # Randomly select an operation
    operation = random.choice(['addition', 'subtraction', 'multiplication'])

    # Calculate the result based on the selected operation
    if operation == "addition":
        res = sum(numbers)
        operation_sign = "+"
    elif operation == "subtraction":
        res = numbers[0]
        for num in numbers[1:]:
            res -= num
        operation_sign = "-"
    elif operation == "multiplication":
        res = 1
        for num in numbers:
            res *= num
        operation_sign = "*"

    # Format the numbers for display
    numbers_str = f" {operation_sign} ".join(map(str, numbers))
    print(f"Calculate the result of: {numbers_str}")

    # Get the user's answer
    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False

    # Check the user's answer
    if user_answer == res:
        print("Correct! You win!")
        return True
    else:
        print(f"Wrong! The correct answer was {res}. Better luck next time!")
        return False






math_roulette_challenge()


